"""Tests for the ISO-3 standardization in notebooks/iso_codes.py.

ISO-3 codes are the merge key joining the NSF, World Bank, and DGBAS tables. A
mapping that stops resolving corrupts every figure downstream. It does not raise.
These tests cover the cases that fail silently: the manual overrides for NSF labels,
the display-name fixes keyed on pycountry's own spellings, and Kosovo, which has no
pycountry entry at all.
"""

import pycountry
import pytest

import iso_codes


# pycountry ships no type stubs. The iteration is correct at runtime.
VALID_ISO3 = {country.alpha_3 for country in pycountry.countries}  # type: ignore

# Kosovo has no ISO 3166-1 assignment and so no pycountry entry. The World Bank
# uses XKX, and iso_codes carries it as a special case at both ends.
KOSOVO = "XKX"


class TestNameToIso3:
    @pytest.mark.parametrize(
        "name, expected",
        [
            ("United States", "USA"),
            ("Russian Federation", "RUS"),
            ("Taiwan, Province of China", "TWN"),
            ("Türkiye", "TUR"),
        ],
    )
    def test_resolves_pycountry_names(self, name, expected):
        assert iso_codes.name_to_iso3(name) == expected

    def test_returns_none_for_unresolvable_name(self):
        """The NSF loader relies on None to trigger the nsf_iso_map fallback."""
        assert iso_codes.name_to_iso3("Atlantis") is None

    def test_returns_none_for_regional_aggregates(self):
        """Aggregate rows are dropped by name. None of them resolves to a country."""
        for label in ["Other Europe", "Middle East", "Unassigned"]:
            assert iso_codes.name_to_iso3(label) is None


class TestIso3ToName:
    def test_resolves_standard_code(self):
        assert iso_codes.iso3_to_name("JPN") == "Japan"

    def test_kosovo_special_case(self):
        """XKX is absent from pycountry. iso_codes handles it explicitly."""
        assert iso_codes.iso3_to_name(KOSOVO) == "Kosovo"

    def test_raises_on_unknown_code(self):
        """A loud failure here keeps an unmapped code out of the merged table."""
        with pytest.raises(KeyError):
            iso_codes.iso3_to_name("ZZZ")


class TestNsfOverrides:
    """nsf_iso_map covers NSF labels that pycountry cannot resolve on its own,
    including ones carrying a trailing footnote letter ('Serbiac', 'West Banke')."""

    def test_every_override_is_a_valid_iso3(self):
        invalid = {
            name: code
            for name, code in iso_codes.nsf_iso_map.items()
            if code not in VALID_ISO3 and code != KOSOVO
        }
        assert not invalid, f"overrides pointing at unknown ISO-3 codes: {invalid}"

    def test_every_override_resolves_to_a_name(self):
        """The loader relabels by code. Each code must survive the return trip."""
        for code in iso_codes.nsf_iso_map.values():
            assert iso_codes.iso3_to_name(code)

    def test_defunct_union_folds_into_serbia(self):
        """NSF reports Serbia and Montenegro for the early years of the panel."""
        assert iso_codes.nsf_iso_map["Serbia and Montenegrod"] == "SRB"
        assert iso_codes.nsf_iso_map["Montenegroc"] == "MNE"

    def test_footnote_suffixed_labels_are_covered(self):
        for label in ["Serbiac", "Gaza Stripe", "West Banke"]:
            assert label in iso_codes.nsf_iso_map


class TestCountryNameFixes:
    """country_name_fixes is keyed on the names iso3_to_name returns, i.e. pycountry's
    own spellings. A pycountry rename stops the key from matching. The rename then
    does nothing, and the old label reaches the figures."""

    def test_keys_are_current_pycountry_names(self):
        produced = {country.name for country in pycountry.countries}  # type: ignore
        stale = set(iso_codes.country_name_fixes) - produced
        assert not stale, f"keys no longer produced by pycountry: {sorted(stale)}"

    def test_fixes_are_applied_after_the_return_trip(self):
        """Spot-check the full code to display-name path used by the loader."""
        for code, expected in [("RUS", "Russia"), ("KOR", "South Korea"), ("TWN", "Taiwan")]:
            name = iso_codes.iso3_to_name(code)
            assert iso_codes.country_name_fixes.get(name, name) == expected

    def test_no_fix_is_a_no_op(self):
        redundant = [k for k, v in iso_codes.country_name_fixes.items() if k == v]
        assert not redundant, f"entries that rename nothing: {redundant}"


class TestNonCountryRows:
    def test_world_and_regions_are_dropped(self):
        for label in ["World", "Europe", "Asia", "Africa"]:
            assert label in iso_codes.non_country_rows

    def test_no_real_country_is_dropped(self):
        """A country name landing in this list would remove it from the panel."""
        wrongly_dropped = [
            label for label in iso_codes.non_country_rows
            if iso_codes.name_to_iso3(label) is not None
        ]
        assert not wrongly_dropped, f"real countries in the drop list: {wrongly_dropped}"
