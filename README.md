# Who Decides What Psychology Says?

__Interpretation of human behavior depends on who writes it.__

Click [here](https://emilinelabbe.github.io/who-decides-what-psych-says/) for the write-up with interactive insights.

## Key findings

1. __Among large science producers, psychology takes up more room in WEIRD countries.__ _(pooled 2011–2022)_ Every WEIRD country in the top 15 devotes at least 2.2% of its output to psychology and every non-WEIRD country devotes 1.3% or less. The UK's rate is almost sixteen times India's.
2. __The US writes more psychology than any other country.__ _(pooled 2011–2022)_ It produced a third of the world's psychology over those twelve years combined (33.8%), nearly double its 17.4% of science. With 4.3% of the global population, that's roughly eight times its population share.
3. __Psychology can be a small part of a country's science and still account for a large share of the world's psychology.__ _(pooled 2011–2022, with annual ranking noted)_ Psychology is under half a percent of China's science output, yet China is the only non-WEIRD member of the top five by volume, and by 2021 it had climbed to second in annual output.
4. __Psychology's center of production is shifting away from the US and its WEIRD peers.__ _(annual, 2003–2022)_ The US share of a single year's world psychology fell from 46.8% in 2003 to 27.7% in 2022 while China's rose from 0.7% to 11.1%. WEIRD countries produced roughly two-thirds of the world's psychology in 2022, down from over 90% in 2003. The 27.7% here and the 33.8% in finding 2 are not in tension: one is the US share of 2022 alone, the other its share of 2011–2022 combined.
5. __Income tracks psychology's share between countries, but not within them.__ _(all country-years, 2003–2022)_ Each doubling of GDP per capita is associated with 77% more psychology per unit of science output (95% CI 53% to 106%; log GDP coefficient 0.826, se 0.109, z = 7.6). Adding country fixed effects reduces that coefficient to 0.252 with SE twice as large. A country growing richer does not measurably shift its own psychology share.

   The estimate is PPML (poisson pseudo-maximum likelihood) on psychology counts, with log total S&E output as an offset, year fixed effects, and standard errors clustered by country (3,879 country-years, 197 countries, 27% of them zero-psychology). PPML is used rather than OLS on a logged share because the outcome has many zeros and variance grows with its mean. Full output in [`01_data_insights.ipynb`](notebooks/01_data_insights.ipynb) under "Panel setup" through "Model comparison".

## Figures

![Top 15 countries by science output, ranked by psychology's share of national science output, 2011–2022](figures/psych_share_ranked.png)
![Psychology publications by country, 2011–2022 total](figures/main_map.png)
![Psychology output against total science output, top 15 countries, 2011–2022](figures/science_vs_psych_scatter.png)
![Annual share of world psychology publications, five largest producers, 2003–2022](figures/global_share_overtime.png)

## Repository layout

```
├── notebooks/
│   ├── 00_data_processing.ipynb    # builds the merged country-year table
│   ├── 01_data_insights.ipynb      # analysis, models, and figures
│   ├── iso_codes.py                # country-name standardization, NSF table loader
│   └── figure_style.py             # palette, Plotly template, figure helpers
├── data/
│   ├── raw/                        # NSF, World Bank, and DGBAS files as downloaded
│   ├── processed/                  # publication_data.csv, written by notebook 00
│   └── README.md                   # sources, retrieval details, licenses
├── tests/                          # unit tests for iso_codes.py
├── figures/                        # PNG figures, written by notebook 01
├── docs/                           # GitHub Pages write-up
│   ├── index.html                  # the article
│   ├── style.css
│   └── js/
│       ├── charts.js               # renders the specs, responsive hover labels
│       └── chart-data.js           # Plotly specs, written by notebook 01
└── requirements.txt
```

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
Tests cover the ISO-3 standardization in `notebooks/iso_codes.py`, the merge key joining all
three data sources.

Notebook order: 
1. `00_data_processing.ipynb` builds `data/processed/publication_data.csv` from the raw NSF, World Bank, and DGBAS files
2. `01_data_insights.ipynb` produces the figures in `figures/` and the chart data for the write-up. 

See [data/README.md](data/README.md) for raw data sources and licenses.