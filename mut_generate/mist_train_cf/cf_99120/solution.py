"""
QUESTION:
Create a function called `update_ingredients` that takes a list of ingredients for a traditional Italian tiramisu recipe and returns an updated list with the non-vegan ingredients replaced with their vegan alternatives. The function should replace the following non-vegan ingredients: egg yolks, milk, heavy cream, and mascarpone cheese, with aquafaba or silken tofu, non-dairy milk, non-dairy heavy cream alternative, and vegan cream cheese or cashew cream cheese respectively. The function should also consider replacing traditional ladyfingers with vegan ladyfingers or vegan sponge cake.
"""

def update_ingredients(ingredients):
    """
    Updates a list of ingredients for a traditional Italian tiramisu recipe to make it vegan-friendly.

    Args:
        ingredients (list): A list of ingredients for the traditional tiramisu recipe.

    Returns:
        list: An updated list of ingredients with non-vegan ingredients replaced with their vegan alternatives.
    """
    vegan_alternatives = {
        'egg yolks': '6 tablespoons aquafaba or 1/2 cup silken tofu',
        'milk': '2/3 cup almond milk or any other non-dairy milk',
        'heavy cream': '1 1/4 cups coconut cream or any other non-dairy heavy cream alternative',
        'mascarpone cheese': '1 pound vegan cream cheese or cashew cream cheese',
        'ladyfingers': '24 vegan ladyfingers or vegan sponge cake'
    }

    updated_ingredients = []
    for ingredient in ingredients:
        for non_vegan, vegan in vegan_alternatives.items():
            if non_vegan in ingredient.lower():
                updated_ingredients.append(ingredient.replace(non_vegan, vegan))
                break
        else:
            updated_ingredients.append(ingredient)

    return updated_ingredients