"""
QUESTION:
Write a function `calculate_average_ratings(ratings)` that takes in a list of dictionaries `ratings` where each dictionary contains the keys 'product', 'date', and 'rating'. The function should calculate the average rating for each product and return a dictionary with product names as keys and average ratings as values. The input list can contain multiple ratings for each product, and the function should handle this by calculating the average rating for each product.
"""

def entance(ratings):
    product_ratings = {}
    product_counts = {}
    
    for entry in ratings:
        product = entry['product']
        rating = entry['rating']
        
        if product in product_ratings:
            product_ratings[product] += rating
            product_counts[product] += 1
        else:
            product_ratings[product] = rating
            product_counts[product] = 1
    
    average_ratings = {}
    for product, total_rating in product_ratings.items():
        average_ratings[product] = total_rating / product_counts[product]
    
    return average_ratings