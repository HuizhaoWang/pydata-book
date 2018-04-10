from collections import defaultdict,OrderedDict,Counter
from pandas import DataFrame,Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
import json

def get_count(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 0
    return counts
    
def get_count2(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

def get_allTzRecords(path):
    records = [json.loads(line) for line in open(path) ]
    time_zones = [record["tz"] for record in records if 'tz' in record] 
    return time_zones

#对字典进行排序
def top_counts(count_dict,n=10):
    value_key_pairs = [(number,tz) for tz,number in count_dict.items()]
    value_key_pairs.sort(reverse=True)
    return value_key_pairs[0:n]



def main():
    pass

if __name__ == '__main__':
   
    path = '/home/whz/Documents/pydata-book/datasets/bitly_usagov/example.txt'
    time_zones = get_allTzRecords(path)

    # counts2 = get_count2(time_zones)
    # count = top_counts(counts2)
    # print(count)

    counts = Counter(time_zones)    
    top_ten = counts.most_common(10)
    # print(top_ten)

    # index = range(1,len(top_ten)+1)
    # colume = ["time_zone","number"]
    # frame = DataFrame(data=top_ten,index=index,columns=colume)
    # print(frame.name)
    # print(frame["number"])

    records = [json.loads(line) for line in open(path) ]
    frame = DataFrame(records)
    tz_counts = frame["tz"].value_counts()
    # print(type(tz_counts))
    # print(tz_counts.values)
    # print(tz_counts[:10].index)

    #将缺少的值,用字符串"unknow"表示出来
    clean_tz = frame["tz"].fillna("")
    clean_tz[clean_tz == ""] = "unknow"
    clean_tz_counts = Series(clean_tz.value_counts()[:10])
    clean_tz_counts.plot(kind="barh")
    pl.show()
    
