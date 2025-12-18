"""
QUESTION:
Implement a function `count_unique_categories` that takes a list of tuples representing product data, where each tuple contains a product name and a list of categories. The function should return a dictionary containing the count of unique categories for each product, ignoring duplicate product names.
"""

def count_unique_categories(products):
    unique_categories_count = {}
    for product, categories in products:
        unique_categories = set(categories)
        if product in unique_categories_count:
            unique_categories_count[product] = max(len(unique_categories), unique_categories_count[product])
        else:
            unique_categories_count[product] = len(unique_categories)
    return unique_categories_count