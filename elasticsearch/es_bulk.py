import pandas as pd
import numpy as np
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import math

es = Elasticsearch("http://192.168.64.199:9200/")

# Load dataset
data = pd.read_excel('data/twitter_QA_pair_re.xlsx')

result_dict = dict()
rowNum = 0
for i in range(data['Unnamed: 0'].count()):
    # len(list(data.iloc[i])) -> 한 row에 컬럼 갯수.. 83개임
    temp = dict()
    for j in range(len(list(data.iloc[i]))-1):
        #if not np.nan:
        #if not math.isnan(data.iloc[i][j+1]):
        #if (data.iloc[i][j] != np.nan) and (data.iloc[i][j+1] != np.nan):
        if type(data.iloc[i][j+1]) is str:
            temp[data.iloc[i][j]] = data.iloc[i][j+1]
        else:
            break
            #temp[i] = {data.iloc[i][j]:data.iloc[i][j+1]}
        result_dict[i] = temp

docs = []
for cnt in range(len(result_dict)):
    for key, value in result_dict[cnt].items(): 
        docs.append({
            '_index':'test_dialogs_10',
            '_type':'_doc',
            '_id': str(cnt+1),
            '_source': {
                'type' : 1,
                'question' : key,
                'answer' : value}
        })

helpers.bulk(es, docs)