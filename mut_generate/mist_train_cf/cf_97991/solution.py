"""
QUESTION:
Create a function `recommend_dish` that takes a list of ingredients as input and returns a recommended dish based on pre-defined rules. The rules consider factors such as cuisine type, cooking method, and dietary restrictions. The function should return a string representing the name of the recommended dish. The input list of ingredients will contain items such as 'Salt', 'Pepper', 'Onion', and 'Garlic'.
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