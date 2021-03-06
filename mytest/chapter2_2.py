import pandas as pd
from pandas import DataFrame,Series

#从文件中分别读出数据
unames = ['user_id','gender','age','occupation','zip']
path_users = "/home/whz/Documents/pydata-book/datasets/movielens/users.dat"
users  = pd.read_table(filepath_or_buffer=path_users,sep="::",header=None,names=unames,engine="python")
# print("===============user===============")
# user_top5 = users[:5]
# print(user_top5)

mnames = ['movie_id','title','genres']
path_movies = "/home/whz/Documents/pydata-book/datasets/movielens/movies.dat"
movies = pd.read_table(path_movies,sep="::",header=None,names=mnames,engine='python')
# print("===============movie===============")
# movie_top5 = movies[:5]
# print(movie_top5)

rnames = ['user_id','movie_id','rating','timestamp']
path_ratings = "/home/whz/Documents/pydata-book/datasets/movielens/ratings.dat"
ratings = pd.read_table(path_ratings,sep="::",header=None,names=rnames,engine='python')
# print("==============rating==============")
# rating_top5 = ratings[:5]
# print(rating_top5)

# print('-------------------------------')
# data1 = pd.merge(users,ratings)
# print(data1)
# print('================================')
# data2 = pd.merge(data1,movies)
# print(data2)

# data3 = pd.merge(movies,data1)
# print(data3)

#合并三个数据表里的数据到一张表格中
data = DataFrame(pd.merge(pd.merge(ratings,users),movies))
# print(type(data))

#分别计算每一部电影男女的各自均分
mean_ratings = pd.pivot_table(data,values="rating",index='title',columns="gender",aggfunc="mean")
# print(mean_ratings)

#统计出每一部电影被点评的次数
ratings_by_title = data.groupby(by="title").size()
# print(type(ratings_by_title))

#过滤掉评分数据不足250条的电影,即找出一定程度上的热门电影
active_titles = ratings_by_title[ratings_by_title.values>250]
# active_titles = ratings_by_title.index[ratings_by_title>250]
# print(active_titles)

#获取评论数目超过250条数据均分
mean_ratings = DataFrame(mean_ratings.ix[active_titles.index])
#print(mean_ratings)

#了解女性最喜欢看的电影,我们可以对F进行排序
top_Female_ratings = mean_ratings.sort_values(by='F',ascending=False)
# print(top_Female_ratings[:10])

#找出男女分歧最大的电影
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
#sorted_by_diff = mean_ratings.sort_values(by='diff',ascending=False)
#也可以先sort,sort之后在进行反序
sorted_by_diff = mean_ratings.sort_values(by='diff')[::-1]
print(sorted_by_diff[:15])

#如果不考虑男女性别之间的差距,只是想找出分歧最大的电影,则可以计算得分数据的方差或者标准差
rating_std_by_title = Series(data.groupby(by='title').rating.std())
print(type(rating_std_by_title))
print(rating_std_by_title[:5])
rating_std_by_title.ix[active_titles.index]
print(rating_std_by_title[:5])

