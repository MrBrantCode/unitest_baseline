"""
QUESTION:
Write a function `calculate_overall_assessment` that calculates the overall assessment for each product in a given dataset. The overall assessment is the sum of the product of the rating and its corresponding weight for each feature of the product. The function should take two parameters: a dictionary `data` containing the product information with keys 'product_id', 'feature_id', and 'rating', and a dictionary `weights` containing the weights for each feature_id. The function should return a dictionary where the keys are the product ids and the values are their overall assessments.
"""

import pandas as pd

def calculate_overall_assessment(data, weights):
    df = pd.DataFrame(data)
    df['weight'] = df['feature_id'].map(weights)
    df['adjusted_rating'] = df['rating'] * df['weight']
    overall_assessment = df.groupby('product_id')['adjusted_rating'].sum().to_dict()
    return overall_assessment