"""
QUESTION:
Replace the following function in the veganize_ingredients function to modify a list of ingredients for a vegan diet. The input is a list of strings representing the ingredients and their quantities. The output is a list of strings representing the modified ingredients and their quantities that are suitable for a vegan diet. The function should replace non-vegan ingredients with their vegan alternatives.
"""

def veganize_ingredients(ingredients):
    """
    This function takes a list of ingredients and their quantities, 
    and returns a new list with non-vegan ingredients replaced with their vegan alternatives.
    """
    vegan_alternatives = {
        'egg yolks': 'aquafaba or silken tofu',
        'milk': 'almond milk or any other non-dairy milk',
        'heavy cream': 'coconut cream or any other non-dairy heavy cream alternative',
        'mascarpone cheese': 'vegan cream cheese or cashew cream cheese',
        'ladyfingers': 'vegan ladyfingers or vegan sponge cake'
    }

    vegan_ingredients = []
    for ingredient in ingredients:
        for non_vegan, vegan in vegan_alternatives.items():
            if non_vegan in ingredient.lower():
                ingredient = ingredient.replace(non_vegan, vegan)
        vegan_ingredients.append(ingredient)

    return vegan_ingredients