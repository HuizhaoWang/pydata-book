import pandas as pd 


#获取指定年数的文件信息
def get_path(year):
    path_pre = "/home/whz/Documents/pydata-book/datasets/babynames/yob"
    return path_pre+str(year)+".txt"

#读取txt的内容
names1880 = pd.DataFrame(pd.read_csv(filepath_or_buffer=get_path(1880),sep=",",names=['name','sex','briths'])) 
print(names1880.groupby(by="sex").briths.sum())                                                 

