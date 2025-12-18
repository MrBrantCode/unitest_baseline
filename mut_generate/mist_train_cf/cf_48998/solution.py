"""
QUESTION:
Create a function called `fruit_distribution` that takes the following parameters: 
- `s`: a list of strings, where each string is in the format "X fruit_name" representing the quantity of a fruit present in a basket
- `n`: an integer representing the total sum of fruits in the basket
- `fruits`: a list of strings representing all the possible types of fruits
- `servings`: a dictionary where keys are the fruit names and values represent the number of servings provided by each fruit
- `max_servings`: a dictionary where keys are the fruit names and values represent the maximum number of servings that can be made for each fruit

The function should return a dictionary where keys are the fruit names and values represent the quantity of servings of each fruit, considering the maximum number of servings constraint. The dictionary should only include fruits with a non-zero count of servings.
"""

def fruit_distribution(s, n, fruits, servings, max_servings):
    fruit_quantities = {}
    for elem in s:
        num, fruit = elem.split()
        fruit_quantities[fruit] = int(num)

    result = {fruit: 0 for fruit in fruits}

    remaining_quantity = n - sum(fruit_quantities.values())
    while remaining_quantity > 0:
        for fruit in fruits:
            if fruit not in fruit_quantities:
                additional_servings = min(remaining_quantity // servings[fruit],
                                          max_servings[fruit] - result[fruit])
                result[fruit] += additional_servings
                remaining_quantity -= additional_servings * servings[fruit]

    for fruit, quantity in fruit_quantities.items():
        if quantity > 0:
            result[fruit] = min(result[fruit] + quantity // servings[fruit], max_servings[fruit])

    result = {fruit: servings for fruit, servings in result.items() if servings > 0}

    return result