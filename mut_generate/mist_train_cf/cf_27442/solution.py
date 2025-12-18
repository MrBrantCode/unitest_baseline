"""
QUESTION:
Implement a function `count_api_categories(api_endpoints)` that takes a list of API endpoints as input, where each endpoint is a string in the format "category_endpoint". The function should return a dictionary where the keys are the unique API categories (with uppercase and lowercase treated as equivalent) and the values are the counts of endpoints belonging to each category.
"""

def count_api_categories(api_endpoints):
    category_counts = {}
    
    for endpoint in api_endpoints:
        category = endpoint.split('_')[0].lower()  # Extract category and convert to lowercase
        category_counts[category] = category_counts.get(category, 0) + 1  # Increment count for the category
        
    return category_counts