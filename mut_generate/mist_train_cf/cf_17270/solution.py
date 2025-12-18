"""
QUESTION:
Implement a function `average_rating` that calculates and returns the average rating for a given product, given a list of ratings. The function should take two parameters: `product_id` and `ratings`. The `ratings` parameter is a list of tuples where each tuple contains a product ID and a rating value. The function should return the average rating for the specified product as a floating-point number. 

The function should handle the case where there are no ratings for the specified product, in which case it should return 0.0.
"""

def average_rating(product_id, ratings):
    """
    Calculate and return the average rating for a given product.

    Args:
        product_id (int): The ID of the product.
        ratings (list): A list of tuples where each tuple contains a product ID and a rating value.

    Returns:
        float: The average rating for the specified product.
    """
    # Filter the ratings to only include the specified product
    product_ratings = [rating for product, rating in ratings if product == product_id]

    # If there are no ratings for the product, return 0.0
    if not product_ratings:
        return 0.0

    # Calculate the average rating
    average = sum(product_ratings) / len(product_ratings)

    return average