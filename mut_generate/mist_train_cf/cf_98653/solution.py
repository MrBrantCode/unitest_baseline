"""
QUESTION:
Create a `check_ingredient` method for the `Soap` class that takes an `ingredient_name` parameter and returns a tuple containing the ingredient name and its quantity if the ingredient is present in the soap's ingredients list. If the ingredient is not present, the method should return `None`. The ingredients list is a list of dictionaries where each dictionary contains the keys 'name' and 'quantity'. The `check_ingredient` method should be case-insensitive when comparing the ingredient names.
"""

def check_ingredient(ingredients, ingredient_name):
    for ingredient in ingredients:
        if ingredient['name'].lower() == ingredient_name.lower():
            return (ingredient['name'], ingredient['quantity'])
    return None