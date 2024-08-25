import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
data = {
    'UserID': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'Product': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product D', 'Product C', 'Product D', 'Product E'],
    'Rating': [4, 5, 2, 5, 3, 4, 4, 5, 2]
}
df = pd.DataFrame(data)
pivot_table = df.pivot_table(index='UserID', columns='Product', values='Rating')
pivot_table = pivot_table.fillna(0)
user_similarity = cosine_similarity(pivot_table)
user_similarity_df = pd.DataFrame(user_similarity, index=pivot_table.index, columns=pivot_table.index)
def recommend_products(user_id, pivot_table, user_similarity_df, n_recommendations=2):
    user_ratings = pivot_table.loc[user_id]
    similarity_scores = user_similarity_df.loc[user_id]
    weighted_ratings = pivot_table.T.dot(similarity_scores) / similarity_scores.sum()
    weighted_ratings = weighted_ratings[~pivot_table.columns.isin(user_ratings[user_ratings > 0].index)]
    recommendations = weighted_ratings.nlargest(n_recommendations)
    return recommendations
recommendations = recommend_products(1, pivot_table, user_similarity_df)
print("Recommended Products for User 1:")
print(recommendations)
