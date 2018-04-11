import pandas as pd 

#获取指定年数的文件信息
def get_path(year):
    path_pre = "/home/whz/Documents/pydata-book/datasets/babynames/yob"
    return path_pre+str(year)+".txt"

columns = ['name','sex','briths']

#读取txt的内容
names1880 = pd.DataFrame(pd.read_csv("/home/whz/Documents/pydata-book/datasets/babynames/yob1880.txt",sep=",",names=columns))
print(names1880.groupby(by="sex").briths.sum())   

# 将每一个文件里的数据都读取出来，并且拼接在一起
pieces = []
for year in range(1880,2011):
    path = get_path(year)
    frame = pd.read_csv(path,names=columns)
    frame['year'] = year
    pieces.append(frame)

#将所有的数据整合到单个DataFrame
names = pd.concat(pieces,ignore_index=True)

print(names)
