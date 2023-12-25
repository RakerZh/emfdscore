# emfd
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love png2](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

- This is forked version from emfdscore.

## Improvements
- compatible with latest spacy and pandas package
- `score_docs` using column index for scoring

## Before install

- make sure your python version >=3.12 in your environment
- install spacy and en_core_web_sm
  see [spacy usage](https://spacy.io/usage)

## Install 

`
pip install emfd
`

## Usage
- emfd
```python
import pandas as pd
from emfdscore.scoring import score_docs
df = pd.read_csv("your_data_set.csv")
num_docs = len(df)
DICT_TYPE = 'emfd'
PROB_MAP = 'all' # or single
SCORE_METHOD = 'bow' # or more options
OUT_METRICS = 'sentiment' # or vice-virtue
OUT_CSV_PATH = './your_output.csv'
column_index = 0
df = score_docs(df,DICT_TYPE,PROB_MAP,SCORE_METHOD,OUT_METRICS,num_docs,column_index)
df.to_csv(OUT_CSV_PATH, index=False)
```

## Future
- polars implementations
- vectorized operations

## Other
When using eMFDscore, please consider giving this repository a star (top right corner) and citing the following article:  
Hopp, F. R., Fisher, J. T., Cornell, D., Huskey, R., & Weber, R. (2020). The extended Moral Foundations Dictionary (eMFD): Development and applications of a crowd-sourced approach to extracting moral intuitions from text. _Behavior Research Methods_, https://doi.org/10.3758/s13428-020-01433-0 

eMFDscore is dual-licensed under GNU GENERAL PUBLIC LICENSE 3.0, which permits the non-commercial use, distribution, and modification of the eMFDscore package. Commercial use of the eMFDscore requires an [application](https://forms.gle/RSKzZ2DvDyaprfeE8).

## Applications 
The eMFD has been used in the following applications (ordered by date of publication):
- [Harris, C., Myers, A., & Kaiser, A. (2022). Being Seen: How Markets Impact Our Moral Sentiments. Available at SSRN: https://ssrn.com/abstract=3997378 or http://dx.doi.org/10.2139/ssrn.3997378](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3997378) 
- [Malik, M., Hopp, F. R., Chen, Y., & Weber, R. (2021). Does Regional Variation in Pathogen Prevalence Predict the Moralization of Language in COVID-19 News? Journal of Language and Social Psychology.](https://doi.org/10.1177%2F0261927X211044194)
- [Chen, Kaiping, Zening Duan, and Sijia Yang. "Twitter as research data: Tools, costs, skill sets, and lessons learned." Politics and the Life Sciences (2021): 1-17.](https://www.cambridge.org/core/journals/politics-and-the-life-sciences/article/twitter-as-research-data/6B31D18C5E2F9B8F9C0301BFB05F1C27)
- [Van Vliet, L. (2021). Moral expressions in 280 characters or less: An Analysis of Politician tweets following the 2016 Brexit referendum vote. Frontiers in Big Data, 4, 49.](https://www.frontiersin.org/articles/10.3389/fdata.2021.699653/full)
- [Priniski, J. H., Mokhberian, N., Harandizadeh, B., Morstatter, F., Lerman, K., Lu, H., & Brantingham, P. J. (2021). Mapping Moral Valence of Tweets Following the Killing of George Floyd. arXiv preprint arXiv:2104.09578.](https://arxiv.org/abs/2104.09578)
- [Hopp, F. R., Fisher, J. T., & Weber, R. (2020). A graph-learning approach for detecting moral conflict in movie scripts. Media and Communication, 8(3), 164.](https://www.cogitatiopress.com/mediaandcommunication/article/view/3155)

