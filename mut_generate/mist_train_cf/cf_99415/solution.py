"""
QUESTION:
Create a function `veganize_tiramisu` that takes a list of ingredients as input and returns the updated list of ingredients with non-vegan items replaced with vegan alternatives. The original ingredients are: 
- 6 egg yolks
- 3/4 cup white sugar
- 2/3 cup milk
- 1 1/4 cups heavy cream
- 1/2 teaspoon vanilla extract
- 1 pound mascarpone cheese
- 1/4 cup strong brewed coffee
- 2 tablespoons rum
- 24 ladyfingers
- 2 tablespoons cocoa powder 
Replace the non-vegan ingredients with the following vegan alternatives:
- egg yolks: aquafaba or silken tofu
- milk: almond milk or any other non-dairy milk
- heavy cream: coconut cream or any other non-dairy heavy cream alternative
- mascarpone cheese: vegan cream cheese or cashew cream cheese
- ladyfingers: vegan ladyfingers or vegan sponge cake
"""

def veganize_tiramisu(ingredients):
    non_vegan_ingredients = {
        '6 egg yolks': '6 tablespoons aquafaba or 1/2 cup silken tofu',
        '2/3 cup milk': '2/3 cup almond milk or any other non-dairy milk',
        '1 1/4 cups heavy cream': '1 1/4 cups coconut cream or any other non-dairy heavy cream alternative',
        '1 pound mascarpone cheese': '1 pound vegan cream cheese or cashew cream cheese',
        '24 ladyfingers': '24 vegan ladyfingers or vegan sponge cake'
    }

    vegan_ingredients = []
    for ingredient in ingredients:
        if ingredient in non_vegan_ingredients:
            vegan_ingredients.append(non_vegan_ingredients[ingredient])
        else:
            vegan_ingredients.append(ingredient)

    return vegan_ingredients