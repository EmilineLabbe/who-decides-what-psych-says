# Data sources and licensing

All files in `raw/` retrieved July 2026.

| Source | Files | Selection | License |
|---|---|---|---|
| [NSF NCSES, Science & Engineering Indicators](https://ncses.nsf.gov/indicators) | `raw/nsf/*.xlsx` | Tables SPBS-2 (all S&E articles) and SPBS-15 (psychology), fractional counts by country, 2003–2022 | [US government work, free to use](https://ncses.nsf.gov/indicators/permissions) |
| [World Bank DataBank, WDI](https://databank.worldbank.org/source/world-development-indicators) | `raw/wbi/*.csv` | 16 series (below), all countries, 2003–2022. `..._Data.csv` holds values, `..._Series - Metadata.csv` holds definitions | [CC BY 4.0](https://datacatalog.worldbank.org/public-licenses) |
| [DGBAS, National Statistics, R.O.C. (Taiwan)](https://eng.stat.gov.tw/cl.aspx?n=4015) | `raw/dgbas/*.csv` | *Principal Figures (2008 SNA)*: mid-year population and per capita GDP, 2003–2022 | [OGDL-Taiwan-1.0](https://eng.stat.gov.tw/cp.aspx?n=2313) |

World Bank series codes, grouped as in `00_data_processing.ipynb`:

- income - `NY.GDP.PCAP.CD`, `NY.GDP.PCAP.PP.CD`, `NY.GDP.PCAP.PP.KD`, `NY.GNP.PCAP.CD`, `NY.GNP.PCAP.PP.CD`, `NY.GNP.PCAP.PP.KD`
- education - `SE.TER.ENRR`, `SE.XPD.TOTL.GD.ZS`, `SE.XPD.TOTL.GB.ZS`, `SE.XPD.TERT.ZS`
- research capacity - `GB.XPD.RSDV.GD.ZS`, `SP.POP.SCIE.RD.P6`
- connectivity and urbanisation - `IT.NET.USER.ZS`, `SP.URB.TOTL.IN.ZS`
- population and science base - `SP.POP.TOTL`, `IP.JRN.ARTC.SC`

## Modifications

`00_data_processing.ipynb` drops NSF regional aggregate rows, standardises country labels to ISO-3 (`notebooks/iso_codes.py`), converts World Bank `..` sentinels to missing, reshapes both sources to one row per country-year, and merges them. Taiwan has no World Bank rows. DGBAS population and GDP per capita stand in, and those rows carry `data_source_flag`.

## Reuse

`processed/publication_data.csv` derives from all three sources and stays subject to their terms:

> NSF NCSES, *Science & Engineering Indicators*; World Bank, *World Development Indicators* (CC BY 4.0, modified: reshaped and merged); DGBAS, National Statistics, R.O.C. (Taiwan).
