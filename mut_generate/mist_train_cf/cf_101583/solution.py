"""
QUESTION:
Create a function called `veganize_tiramisu` to modify the traditional Italian tiramisu recipe to make it vegan. The function should take the original ingredient list as input and return the updated vegan ingredient list.
"""

def veganize_tiramisu(original_ingredients):
    """
    Modifies the traditional Italian tiramisu recipe to make it vegan.
    
    Parameters:
    original_ingredients (list): A list of the original ingredients.
    
    Returns:
    list: The updated vegan ingredient list.
    """
    replacements = {
        "6 egg yolks": "6 tablespoons aquafaba or 1/2 cup silken tofu",
        "2/3 cup milk": "2/3 cup almond milk or any other non-dairy milk",
        "1 1/4 cups heavy cream": "1 1/4 cups coconut cream or any other non-dairy heavy cream alternative",
        "1 pound mascarpone cheese": "1 pound vegan cream cheese or cashew cream cheese",
        "24 ladyfingers": "24 vegan ladyfingers or vegan sponge cake"
    }
    
    vegan_ingredients = []
    for ingredient in original_ingredients:
        if ingredient in replacements:
            vegan_ingredients.append(replacements[ingredient])
        else:
            vegan_ingredients.append(ingredient)
    
    return vegan_ingredients