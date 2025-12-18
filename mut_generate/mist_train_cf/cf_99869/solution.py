"""
QUESTION:
Write a function named `sort_animals_by_weight` that takes a JSON data string containing animal names as keys and dictionaries with a 'weight' key as values. Sort the animal names in ascending order based on their weights and return the sorted list of animal names.
"""

import json

def sort_animals_by_weight(json_data):
    """
    Sorts animal names in ascending order based on their weights.
    
    Args:
    json_data (str): A JSON data string containing animal names as keys and dictionaries with a 'weight' key as values.
    
    Returns:
    list: A sorted list of animal names.
    """
    animals = json.loads(json_data)
    return [animal[0] for animal in sorted(animals.items(), key=lambda x: x[1]['weight'])]