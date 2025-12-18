"""
QUESTION:
Compute a weighted average of ratings for each product given a list of product ratings with their corresponding weights. The function `compute_weighted_scores` should take in a list of dictionaries, where each dictionary contains `product_id`, `feature_id`, `rating`, and `weight`. The function should return a dictionary where the keys are the `product_id` and the values are the weighted average scores. Assume that the weights for each feature are already provided and sum up to 1 for each product.
"""

from collections import defaultdict

def compute_weighted_scores(data):
    """
    Compute a weighted average of ratings for each product.

    Args:
        data (list): A list of dictionaries, where each dictionary contains 
                     'product_id', 'feature_id', 'rating', and 'weight'.

    Returns:
        dict: A dictionary where the keys are the 'product_id' and the values 
              are the weighted average scores.
    """
    product_ratings = defaultdict(dict)
    for entry in data:
        product_ratings[entry['product_id']][entry['feature_id']] = (entry['rating'], entry['weight'])

    product_scores = {}
    for product, ratings in product_ratings.items():
        weighted_sum = sum(rating * weight for rating, weight in ratings.values())
        product_scores[product] = weighted_sum

    return product_scores