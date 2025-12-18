"""
QUESTION:
Create a function named `product_limit` that takes a tuple of numbers and a numerical limit as input. The function should calculate the aggregated product of consecutive components in the tuple until the product reaches or exceeds the given limit. The function should return the aggregated product.
"""

def product_limit(tup, limit):
    agg_product = 1  
    for val in tup:
        if agg_product*val <= limit:  
            agg_product *= val  
        else:
            break  
        
    return agg_product