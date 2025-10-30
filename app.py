# 导入必要的库
import pandas as pd 
import numpy as np 
from sklearn.metrics.pairwise import cosine_similarity 
 # 加载数据 
movies = pd.read_csv('C:/Users/31579/Downloads/archive/ml-100k/movies.csv') 
ratings = pd.read_csv('C:/Users/31579/Downloads/archive/ml-100k/ratings.csv')
 # 查看数据长什么样 
print("电影数据：") 
print(movies.head()) # 显示前5行 
print("\n评分数据：") 
print(ratings.head())


# 检查缺失值 
print(ratings.isnull().sum()) 
 # 创建一个“用户-电影”评分矩阵 # 这个矩阵的行是用户，列是电影，值是评分 
ratings_matrix = ratings.pivot_table(index='user_id', columns='movie_id', values='rating') 
 # 查看矩阵形状 
print(f"评分矩阵的形状：{ratings_matrix.shape}") 
 # 用0填充缺失值（因为协同过滤计算需要数值） 
ratings_matrix.fillna(0, inplace=True) 
 # 再次查看填充后的矩阵 
print(ratings_matrix.head())


# 计算电影之间的余弦相似度 
movie_similarity = cosine_similarity(ratings_matrix.T) # .T 表示对矩阵进行转置，让电影变成行 
 # 将相似度矩阵转换为DataFrame，方便查看 
movie_similarity_df = pd.DataFrame(movie_similarity, index=ratings_matrix.columns, columns=ratings_matrix.columns) 
print(movie_similarity_df.head())


def get_similar_movies(movie_name, min_ratings=10):     # 通过电影名找到它的ID     
    movie_id = movies[movies['title'] == movie_name]['movie_id'].values[0] 
     # 从相似度矩阵中获取该电影与其他所有电影的相似度分数     
    similarity_scores = movie_similarity_df[movie_id] 
     # 将这些分数与原始电影数据合并，方便看到电影名     
    similar_movies = pd.DataFrame({'movie_id':similarity_scores.index,'similarity':similarity_scores.values}).merge(movies,on='movie_id') 
     # 我们可以简单地按相似度分数从高到低排序，并返回前10个     
    return similar_movies.sort_values(by='similarity', ascending=False).head(10) 
 # 输入你喜欢的电影，看看推荐结果！ 
your_favorite_movie = "Forrest Gump (1994)" # 请确保电影名与数据集中的完全一致 
recommendations = get_similar_movies(your_favorite_movie) 
print(f"因为你喜欢《{your_favorite_movie}》，所以我们为你推荐：") 
print(recommendations[['title']]) # 只打印电影名和类型   


import streamlit as st

st.title('🎬 我的简易电影推荐系统')
st.write('发现你可能喜欢的下一部好电影！')

# 创建一个下拉选择框，让用户选择电影
movie_list = movies['title'].values
selected_movie = st.selectbox('选择一部你喜欢的电影：', movie_list)

if st.button('获取推荐'):
    if selected_movie:
        with st.spinner('正在努力寻找相似电影...'):
            recommendations = get_similar_movies(selected_movie)
        st.success('推荐完成！')
        st.write(f"因为你喜欢 **《{selected_movie}》**，所以我们为你推荐：")
        for idx, row in recommendations.iterrows():
            st.write(f"- {row['title']}")
    else:
        st.error('请选择一部电影！')

    