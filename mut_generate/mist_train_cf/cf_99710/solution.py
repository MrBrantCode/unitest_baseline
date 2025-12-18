"""
QUESTION:
Create a `recommend_dish` function that takes a list of ingredients as input and returns a recommended dish based on pre-defined rules. The function should consider the presence of ingredients in the input list and return a dish that can be prepared using those ingredients. The function should return 'No dish recommendation' if no matching dish is found. The input list will only contain ingredients 'Salt', 'Pepper', 'Onion', and 'Garlic'.
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