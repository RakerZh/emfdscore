import pandas as pd
from emfd.scoring import score_docs

def test_emfd():
    df = pd.read_csv("./emfd/template_input.csv")
    df = df.head(10)

    num_docs = len(df)
# emfd mfd mfd2
    DICT_TYPE = 'mfd2'
# all single (only for emfd)
    PROB_MAP = 'all'
# 
    SCORE_METHOD = 'bow'
    OUT_METRICS = 'sentiment'
    OUT_METRICS = 'vice-virtue'
    OUT_CSV_PATH = './tests/mfd2_all_bow_sentiment.csv'

    df = score_docs(df,DICT_TYPE,PROB_MAP,SCORE_METHOD,OUT_METRICS,num_docs)
    df.to_csv(OUT_CSV_PATH, index=False)

