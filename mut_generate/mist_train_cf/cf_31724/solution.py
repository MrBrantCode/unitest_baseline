"""
QUESTION:
Implement the function `orderedsandwich` that takes a list of ingredients as input and returns a string representing the ordered sandwich. The function should handle the following cases:
- A single ingredient: append the string "sandwich" to the ingredient.
- Two ingredients: use the first ingredient as the filling, the second ingredient as the bread, and append the string "sandwich".
- More than two ingredients: use the first ingredient as the filling, the last ingredient as the bread, and any middle ingredients as additional fillings, appending the string "sandwich" at the end.

The function should return the ordered sandwich string, correctly formatted according to the number of ingredients provided.
"""

def orderedsandwich(ingredients):
    if len(ingredients) == 1:
        return f"{ingredients[0]} sandwich"
    elif len(ingredients) == 2:
        return f"{ingredients[0]} and {ingredients[1]} sandwich"
    else:
        filling = ', '.join(ingredients[1:-1])
        return f"{ingredients[0]}{', ' + filling if filling else ''} and {ingredients[-1]} sandwich"