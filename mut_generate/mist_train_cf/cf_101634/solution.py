"""
QUESTION:
Write a function called `sort_animals_by_weight` that takes a JSON object containing animal names as keys and their corresponding weights as values, and returns a list of animal names sorted in ascending order by weight. The input JSON object has the following format: 
{
    "animal_name": {
        "weight": weight_value
    }
}
The function should return a list of animal names. The weights of the animals are assumed to be unique.
"""

import json

def sort_animals_by_weight(json_data):
    """
    Sorts animal names in ascending order by weight.

    Args:
    json_data (dict): A dictionary containing animal names as keys and their corresponding weights as values.

    Returns:
    list: A list of animal names sorted in ascending order by weight.
    """
    # Load JSON data
    animals = json_data
    # Sort animals based on weight
    sorted_animals = sorted(animals.items(), key=lambda x: x[1]['weight'])
    # Return a list of sorted animal names
    return [animal[0] for animal in sorted_animals]