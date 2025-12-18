"""
QUESTION:
Create a function `update_ingredients` that takes a list of strings representing the original ingredients and their quantities, and returns a list of strings representing the updated ingredients with their quantities, replacing non-vegan ingredients with their vegan alternatives.
"""

def update_ingredients(original_ingredients):
    vegan_alternatives = {
        '6 egg yolks': '6 tablespoons aquafaba or 1/2 cup silken tofu',
        '2/3 cup milk': '2/3 cup almond milk or any other non-dairy milk',
        '1 1/4 cups heavy cream': '1 1/4 cups coconut cream or any other non-dairy heavy cream alternative',
        '1 pound mascarpone cheese': '1 pound vegan cream cheese or cashew cream cheese',
        '24 ladyfingers': '24 vegan ladyfingers or vegan sponge cake'
    }

    updated_ingredients = []
    for ingredient in original_ingredients:
        if ingredient in vegan_alternatives:
            updated_ingredients.append(vegan_alternatives[ingredient])
        else:
            updated_ingredients.append(ingredient)

    return updated_ingredients