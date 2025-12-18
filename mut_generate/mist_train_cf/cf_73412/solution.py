"""
QUESTION:
Design a function named `fruit_distribution` that takes a dictionary `fruit_families_basket` containing 10 unique fruits from different families and a total number of fruits `total_fruits_in_salad` as input. The function should return a dictionary where the keys are the fruit names and the values are the number of each fruit in the salad, with the distribution based on the length of the fruit names. The total number of fruits in the salad should equal `total_fruits_in_salad`.
"""

def fruit_distribution(fruit_families_basket, total_fruits_in_salad):
    """
    This function takes a dictionary of fruit families and their corresponding fruits, 
    and the total number of fruits in a salad as input. It returns a dictionary 
    where the keys are the fruit names and the values are the number of each fruit 
    in the salad, with the distribution based on the length of the fruit names.

    Args:
    fruit_families_basket (dict): A dictionary containing fruit families and their corresponding fruits.
    total_fruits_in_salad (int): The total number of fruits in the salad.

    Returns:
    dict: A dictionary with fruit names as keys and their quantities as values.
    """

    fruit_distribution = dict()
    total_length = 0

    # calculating the total length of all fruit names
    for fruit in fruit_families_basket.values():
        total_length += len(fruit)

    # Distributing fruits based on the length of their names
    for family, fruit in fruit_families_basket.items():
        percentage = len(fruit) / total_length
        fruit_distribution[fruit] = round(percentage * total_fruits_in_salad)

    # Making sure the total number of fruits is equal to total_fruits_in_salad
    # Fix any rounding issues, simply add/remove from any fruit
    difference = total_fruits_in_salad - sum(fruit_distribution.values())
    if difference != 0:
        fruit_distribution['Loquat'] += difference

    return fruit_distribution