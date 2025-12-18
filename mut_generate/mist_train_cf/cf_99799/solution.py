"""
QUESTION:
Write a function `calculate_calories` that calculates the total number of calories in a given fruit (excluding banana) based on its weight. The function should take as input a dictionary containing the fruit's name, calories per 100 grams, and weight per 100 grams, and the actual weight of the fruit in grams. The function should return the total number of calories in the given weight of fruit.
"""

def calculate_calories(fruit, weight):
    """
    Calculate the total number of calories in a given fruit (excluding banana) based on its weight.

    Args:
        fruit (dict): A dictionary containing the fruit's name, calories per 100 grams, and weight per 100 grams.
        weight (float): The actual weight of the fruit in grams.

    Returns:
        float: The total number of calories in the given weight of fruit.
    """
    return (fruit['calories'] / 100) * weight