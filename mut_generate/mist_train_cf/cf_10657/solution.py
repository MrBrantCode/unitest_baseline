"""
QUESTION:
Write a function `calculate_overall_rating` that takes in two tables: `product_features` and `feature_weights`. The `product_features` table contains columns `product_id`, `feature_id`, and `rating`, representing the ratings given for each feature of a product. The `feature_weights` table contains columns `feature_id` and `weight`, representing the weights of each feature, where each weight is between 0 and 1, and the sum of all feature weights for a product equals 1. The function should return a table containing the `product_id` and the overall rating for each product, which is the weighted sum of ratings rounded to the nearest integer.
"""

import pandas as pd

def calculate_overall_rating(product_features, feature_weights):
    """
    This function calculates the overall rating for each product by multiplying the rating of each feature by its corresponding weight, 
    summing up these weighted ratings, and rounding the result to the nearest integer.

    Args:
        product_features (pd.DataFrame): A DataFrame containing the product_id, feature_id, and rating for each feature of a product.
        feature_weights (pd.DataFrame): A DataFrame containing the feature_id and weight for each feature.

    Returns:
        pd.DataFrame: A DataFrame containing the product_id and the overall rating for each product.
    """

    # Merge the product_features and feature_weights tables based on the feature_id
    merged_table = pd.merge(product_features, feature_weights, on='feature_id')

    # Multiply the rating by the weight for each feature
    merged_table['weighted_rating'] = merged_table['rating'] * merged_table['weight']

    # Group by product_id and sum up the weighted ratings
    overall_ratings = merged_table.groupby('product_id')['weighted_rating'].sum().round().reset_index()

    # Rename the weighted_rating column to overall_rating
    overall_ratings = overall_ratings.rename(columns={'weighted_rating': 'overall_rating'})

    return overall_ratings