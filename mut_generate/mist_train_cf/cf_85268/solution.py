"""
QUESTION:
Implement a function to rank products based on their comprehensive evaluation. The function should take a list of product evaluations where each evaluation is a tuple of product_id, attribute_id, weight, and rating. The comprehensive evaluation of a product is calculated by summing all the weighted scores of its attributes. If a rating is missing or null, it should be handled by replacing it with 0. The function should return a list of product_ids sorted in descending order of their comprehensive evaluation. 

The function should also provide an option to update the weight of individual attribute scores and accommodate newly added attributes in future implementation.
"""

def rank_products(evaluations):
    """
    This function ranks products based on their comprehensive evaluation.
    
    Parameters:
    evaluations (list): A list of tuples containing product_id, attribute_id, weight, and rating.
    
    Returns:
    list: A list of product_ids sorted in descending order of their comprehensive evaluation.
    """
    
    # Create a dictionary to store the comprehensive evaluation of each product
    product_scores = {}
    
    # Iterate over each evaluation
    for product_id, attribute_id, weight, rating in evaluations:
        # Replace missing or null ratings with 0
        rating = rating if rating is not None else 0
        
        # Calculate the weighted score
        score = weight * rating
        
        # Add the score to the product's comprehensive evaluation
        if product_id in product_scores:
            product_scores[product_id] += score
        else:
            product_scores[product_id] = score
    
    # Sort the products by their comprehensive evaluation in descending order
    sorted_product_ids = sorted(product_scores, key=product_scores.get, reverse=True)
    
    return sorted_product_ids