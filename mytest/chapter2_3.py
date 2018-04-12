import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#获取指定年数的文件信息
def get_path(year):
    path_pre = "/home/whz/Documents/pydata-book/datasets/babynames/yob"
    return path_pre+str(year)+".txt"

columns = ['name','sex','briths']

#读取txt的内容
# names1880 = pd.DataFrame(pd.read_csv("/home/whz/Documents/pydata-book/datasets/babynames/yob1880.txt",sep=",",names=columns))
# print(names1880.groupby(by="sex").briths.sum())   

# 将每一个文件里的数据都读取出来，并且拼接在一起
pieces = []
for year in range(1880,2011):
    path = get_path(year)
    frame = pd.read_csv(path,names=columns)
    frame['year'] = year
    pieces.append(frame)

#将所有的数据整合到单个DataFrame
names =pd.DataFrame(pd.concat(pieces,ignore_index=True))
# print(names)

#pivot_table 透视图
total_births = pd.DataFrame(pd.pivot_table(names,
    index=['name'],values='briths',columns='sex',aggfunc=[np.mean],
    fill_value = 0).head(10))

# print(total_births)
# total_births.plot.barh(title='Total briths by name year sex')
# plt.show()

#求占比
def add_prop(group):
    group['prop'] = group.briths / group.briths.sum()
    return group    

#分组的过程中注意分组的依据,也就是by
names = names.groupby(by=['year','sex']).apply(add_prop)
print(names)




