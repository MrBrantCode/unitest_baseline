"""
QUESTION:
Write a function named `count_items` that takes a dictionary `inventory` as input. The dictionary has two keys: "fruits" and "vegetables". The values corresponding to these keys are lists of fruit and vegetable names. The function should return a dictionary where the keys are the names of fruits and vegetables and the values are their respective counts.
"""

def count_items(inventory):
    result = {}
    for category in inventory:
        for item in inventory[category]:
            if item not in result:
                result[item] = 1
            else:
                result[item] += 1
    return result