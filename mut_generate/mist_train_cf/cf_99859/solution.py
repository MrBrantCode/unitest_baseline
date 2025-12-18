"""
QUESTION:
Create a function `calculate_calories` that takes a fruit dictionary and a weight in grams as input, and calculates the total number of calories based on the calories per 100 grams of the fruit. The fruit dictionary should contain keys for 'name' and 'calories', and the 'calories' value should represent the calories per 100 grams of the fruit. The function should return the total number of calories for the given weight of the fruit. Exclude bananas from the fruits considered.
"""

def calculate_calories(fruit, weight):
    """
    Calculate the total number of calories based on the calories per 100 grams of the fruit.

    Args:
        fruit (dict): A dictionary containing keys for 'name' and 'calories'.
        weight (float): The weight in grams of the fruit.

    Returns:
        float: The total number of calories for the given weight of the fruit.
    """
    if fruit['name'].lower() != 'banana':
        return (fruit['calories'] / 100) * weight
    else:
        return None