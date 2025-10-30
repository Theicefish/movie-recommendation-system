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