"""
QUESTION:
Compute the overall rating for each product given two dictionaries: `feature_ratings` and `feature_weights`, where `feature_ratings` contains the ratings given for each feature of a product and `feature_weights` contains the corresponding weights. The weights are prime numbers between 0 and 1, and the sum of all feature weights for a product is a prime number. The function `compute_overall_rating` should return the overall rating rounded to the nearest prime number. 

The function `compute_overall_rating` should take two dictionaries as input: `feature_ratings` and `feature_weights`. It should return a single integer value representing the overall rating rounded to the nearest prime number.
"""

import math

def compute_overall_rating(feature_ratings, feature_weights):
    """
    Compute the overall rating for a product given its feature ratings and weights.
    
    Args:
    feature_ratings (dict): A dictionary containing ratings for each feature of a product.
    feature_weights (dict): A dictionary containing weights for each feature of a product.
    
    Returns:
    int: The overall rating rounded to the nearest prime number.
    """
    
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    # Compute the weighted sum of ratings
    overall_rating = sum(feature_ratings[feature] * feature_weights[feature] for feature in feature_ratings)
    
    # Round the overall rating to the nearest prime number
    rounded_rating = round(overall_rating)
    while not is_prime(rounded_rating):
        rounded_rating += 1
    
    return rounded_rating