from collections import defaultdict,OrderedDict
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
    value_key_pairs = [(number,tz) for tz,number in counts2.items()]
    value_key_pairs.sort(reverse=True)
    return value_key_pairs[0:n]

def main():
    pass

if __name__ == '__main__':
    path = '/home/whz/Documents/pydata-book/datasets/bitly_usagov/example.txt'
    sequence = get_allTzRecords(path)
    counts2 = get_count2(sequence)
