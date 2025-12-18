"""
QUESTION:
Implement the `calculate_budget` function to calculate the total budget for a specific gift category. The function should take the category name as input and return the total budget for that category. The budget should be calculated by summing up the prices of all gifts in the given category. The function should be able to handle cases where the category is not found or is empty.
"""

def calculate_budget(category):
    """
    Calculate the total budget for a specific gift category.
    
    Args:
    category (str): The name of the gift category.
    
    Returns:
    int: The total budget for the given category.
    """
    gifts = [
        {"name": "Smartwatch", "category": "Electronics", "price": 150},
        {"name": "Headphones", "category": "Electronics", "price": 50},
        {"name": "Coffee Maker", "category": "Home", "price": 100},
        {"name": "Blanket", "category": "Home", "price": 75},
        {"name": "Smart Speaker", "category": "Electronics", "price": 200},
        {"name": "Instant Pot", "category": "Home", "price": 150},
        {"name": "Fitness Tracker", "category": "Electronics", "price": 100},
        {"name": "Air Fryer", "category": "Home", "price": 80},
        {"name": "Kindle", "category": "Electronics", "price": 120},
        {"name": "Bedding Set", "category": "Home", "price": 90}
    ]
    
    budget = 0
    for gift in gifts:
        if gift["category"] == category:
            budget += gift["price"]
    return budget