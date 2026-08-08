# Who Decides What Psychology Says?

__Interpretation of human behavior depends on who writes it.__

Click [here](https://emilinelabbe.github.io/who-decides-what-psych-says/) for the write-up with interactive insights.

## Setup
```bash
pip install -r requirements.txt
```
Run the notebooks in order: `00_data_processing.ipynb` builds `data/processed/publication_data.csv` from the raw NSF, World Bank, and DGBAS files, and `01_data_insights.ipynb` produces the figures in `figures/` and the chart data behind the write-up.

## Key findings
_Figures and findings cover 2011–2022 unless noted._
1. __Psychology's share of national output is highest in the WEIRD world.__ Among the top 15 science producers, every WEIRD country devotes at least 2.2% of its output to psychology and every non-WEIRD country devotes 1.3% or less. The UK's rate is almost sixteen times India's.
2. __The US leads the world in psychology.__ It writes a third of the world's psychology (33.8%), nearly double its 17.4% of science. With 4.3% of the global population, it produces psychology at roughly eight times its population share.
3. __Psychology is 0.45% of China's science output, but the base is large enough that the volume is still substantial.__ In cumulative output, China is the only non-WEIRD member of the top five, though by 2021 it had climbed to second in annual output.
4. __The US share of psychology has nearly halved since 2003.__ It fell from 46.8% to 27.7% of annual world psychology output, while China's rose from 0.7% to 11.1%. WEIRD countries produced two-thirds of the world's psychology publications in 2022, down from 90% in 2003.

## Figures
![psych share ranking](figures/psych_share_ranked.png)
![main map](figures/main_map.png)
![science vs psych scatter](figures/science_vs_psych_scatter.png)
![global psych share over time](figures/global_share_overtime.png)
