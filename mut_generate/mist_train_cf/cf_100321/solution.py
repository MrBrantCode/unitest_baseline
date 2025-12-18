"""
QUESTION:
Write a function `recommend_dish` that takes a list of ingredients as input and returns a dish recommendation based on a set of pre-defined rules. The rules consider factors such as cuisine type, cooking method, and dietary restrictions. The input list will contain a combination of 'Salt', 'Pepper', 'Onion', and 'Garlic'. If no matching dish is found, return 'No dish recommendation'.
"""

def recommend_dish(ingredients):
    if 'Salt' in ingredients and 'Pepper' in ingredients and 'Onion' in ingredients and 'Garlic' in ingredients:
        return 'Spaghetti Carbonara'
    elif 'Salt' in ingredients and 'Pepper' in ingredients and 'Garlic' in ingredients:
        return 'Garlic Shrimp'
    elif 'Salt' in ingredients and 'Pepper' in ingredients and 'Onion' in ingredients:
        return 'French Onion Soup'
    elif 'Salt' in ingredients and 'Pepper' in ingredients:
        return 'Grilled Steak'
    else:
        return 'No dish recommendation'