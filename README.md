# Who Decides What Psychology Says?

__Interpretation of human behavior depends on who writes it.__

Click [here](https://emilinelabbe.github.io/who-decides-what-psych-says/) for the write-up with interactive insights.

## Setup
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
Run notebooks in order: 
1. `00_data_processing.ipynb` builds `data/processed/publication_data.csv` from the raw NSF, World Bank, and DGBAS files
2. `01_data_insights.ipynb` produces the figures in `figures/` and the chart data behind the write-up. 

See [data/README.md](data/README.md) for raw data sources and licenses.

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
├── figures/                        # PNG figures, written by notebook 01
├── docs/                           # GitHub Pages write-up
│   ├── index.html                  # the article
│   └── js/chart-data.js            # Plotly specs, written by notebook 01
├── requirements.txt
└── CITATION.cff
```

## Key findings
_Figures and findings cover 2011–2022 unless noted._
1. __Among large science producers, psychology takes up more room in WEIRD countries.__ Every WEIRD country in the top 15 devotes at least 2.2% of its output to psychology and every non-WEIRD country devotes 1.3% or less. The UK's rate is almost sixteen times India's.
2. __The US writes more psychology than any other country.__ It produces a third of the world's psychology (33.8%), nearly double its 17.4% of science. With 4.3% of the global population, that's roughly eight times its population share.
3. __Psychology can be a small part of a country's science and still account for a large share of the world's psychology.__ Psychology is under half a percent of China's science output, yet China is the only non-WEIRD member of the top five by volume, and by 2021 it had climbed to second in annual output.
4. __Psychology's center of production is shifting away from the US and its WEIRD peers.__ The US share fell from 46.8% to 27.7% of annual world psychology output while China's rose from 0.7% to 11.1%. WEIRD countries produced two-thirds of the world's psychology in 2022, down from 90% in 2003.

## Figures
![psych share ranking](figures/psych_share_ranked.png)
![main map](figures/main_map.png)
![science vs psych scatter](figures/science_vs_psych_scatter.png)
![global psych share over time](figures/global_share_overtime.png)

