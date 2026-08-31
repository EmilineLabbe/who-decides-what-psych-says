"""Country-code standardization and NSF SPBS table loading for 00_data_processing.ipynb.

ISO-3 codes are the merge key across all four data sources. NSF, the World Bank,
and pycountry each spell a handful of countries differently. Explicit override maps
accompany the pycountry lookups.
"""

import pandas as pd
import pycountry
from IPython.display import display


def name_to_iso3(name):
    """
    Get the ISO 3-letter code for a country name.
    """
    try:
        return pycountry.countries.lookup(name).alpha_3
    except LookupError:
        return None


def iso3_to_name(iso):
    """
    Get the country name from an ISO 3-letter code.
    """
    if iso == 'XKX':  # XKX (Kosovo) is not included in pycountry's ISO database
        return 'Kosovo'
    country = pycountry.countries.get(alpha_3=iso)
    if country is None:
        raise KeyError(f"unresolved ISO-3 code: {iso!r}")
    return country.name


# NSF labels requiring manual ISO-3 standardization
nsf_iso_map = {
    'Bahamas, The': 'BHS',
    'Holy See (Vatican City)': 'VAT',
    'Kosovo': 'XKX',
    'Montenegroc': 'MNE',
    'Russia': 'RUS',
    'Serbiac': 'SRB',
    'Serbia and Montenegrod': 'SRB',  # Defunct union; add to modern Serbia's code
    'Turkey': 'TUR',
    'Congo, Democratic Republic of the': 'COD',
    'Congo, Republic of the': 'COG',
    'Côte d’Ivoire': 'CIV',
    'Gambia, The': 'GMB',
    'São Tomé and Príncipe': 'STP',
    'Brunei': 'BRN',
    'Burma': 'MMR',
    'Gaza Stripe': 'PSE',   # NSF's footnoted label for Gaza
    'West Banke': 'PSE',    # NSF's footnoted label for the West Bank
}

# Standardize country names for visualization labels
country_name_fixes = {
    'Bolivia, Plurinational State of': 'Bolivia',
    'Brunei Darussalam': 'Brunei',
    'Cabo Verde': 'Cape Verde',
    'Congo, The Democratic Republic of the': 'Democratic Republic of the Congo',
    'Czechia': 'Czech Republic',
    'Iran, Islamic Republic of': 'Iran',
    "Korea, Democratic People's Republic of": 'North Korea',
    'Korea, Republic of': 'South Korea',
    "Lao People's Democratic Republic": 'Laos',
    'Micronesia, Federated States of': 'Micronesia',
    'Moldova, Republic of': 'Moldova',
    'North Macedonia': 'Macedonia',
    'Russian Federation': 'Russia',
    'Syrian Arab Republic': 'Syria',
    'Taiwan, Province of China': 'Taiwan',
    'Tanzania, United Republic of': 'Tanzania',
    'Türkiye': 'Turkey',
    'Venezuela, Bolivarian Republic of': 'Venezuela',
    'Viet Nam': 'Vietnam',
    'Holy See (Vatican City State)': 'Vatican City',
    'Palestine, State of': 'Palestine',
}

# Regional/world aggregate rows present in every NSF SPBS table
non_country_rows = [
    "World",
    "North America",
    "Central America and Caribbean",
    "South America",
    "Europe",
    "EU-27 and United Kingdoma",
    "EU-27b", "Other Europe",
    "Other Europe, 2020",
    "Middle East",
    "Africa",
    "Asia",
    "Australia and Oceania",
    "Unassigned",
]


def load_nsf_table(path, sheet_name, value_name, drop_cols=None):
    """
    Load one NSF SPBS table (country rows + year columns), drop regional
    aggregates, then standardize to ISO-3.

    """
    raw = pd.read_excel(path, sheet_name=sheet_name, header=3)
    raw = raw.rename(columns={raw.columns[0]: "Country"})

    if drop_cols:
        raw = raw.drop(columns=drop_cols)

    raw = raw[~raw["Country"].isin(non_country_rows)]

    year_cols = [c for c in raw.columns if isinstance(c, (int, float))]

    df = raw.melt(
        id_vars="Country",
        value_vars=year_cols,
        var_name="Year",
        value_name=value_name
    )
    df = df.dropna(subset=[value_name])
    df["Year"] = df["Year"].astype(int)

    df["iso_alpha"] = df["Country"].apply(name_to_iso3)
    df["iso_alpha"] = df["iso_alpha"].fillna(df["Country"].map(nsf_iso_map))

    unmatched_iso = df[df["iso_alpha"].isna()]
    if len(unmatched_iso):
        display(unmatched_iso[["Country", value_name]])

    # Sum NSF labels sharing an ISO code
    df = df.groupby(["iso_alpha", "Year"], as_index=False)[value_name].sum()

    df["Country"] = df["iso_alpha"].apply(iso3_to_name)
    df["Country"] = df["Country"].replace(country_name_fixes)

    unmatched_names = df[df["Country"].isna()]
    if len(unmatched_names):
        display(unmatched_names[["iso_alpha", value_name]])

    print(f"{sheet_name:<16} {df['iso_alpha'].nunique():>4} countries  "
          f"{len(unmatched_iso)} unmatched ISO codes  {len(unmatched_names)} unmatched names")

    return df
