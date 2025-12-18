"""
QUESTION:
Implement the `recommender` function, which takes a pandas DataFrame `df` containing recipe data as input and returns a list of recommended recipe IDs. The input DataFrame `df` should have a "rating" column and a "recipe_id" column. The function should return the IDs of the top 5 recipes with the highest ratings.
"""

import pandas as pd

def recommender(df):
    recommended_recipes = df.sort_values(by="rating", ascending=False).head(5)["recipe_id"].tolist()
    return recommended_recipes