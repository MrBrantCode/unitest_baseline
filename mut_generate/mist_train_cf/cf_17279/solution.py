"""
QUESTION:
Create a function named `count_animal_types` that takes a list of strings as input, where each string represents a person's name followed by a colon and a list of their pet animals, with the animals separated by commas. The function should return a dictionary where the keys are the names and the values are the number of different types of pet animals owned.
"""

def count_animal_types(pets):
    """
    This function takes a list of strings as input, where each string represents a person's name 
    followed by a colon and a list of their pet animals, with the animals separated by commas.
    It returns a dictionary where the keys are the names and the values are the number of different 
    types of pet animals owned.

    Args:
    pets (list): A list of strings representing people's names and their pet animals.

    Returns:
    dict: A dictionary where keys are names and values are the number of different pet animal types.
    """
    pet_dict = {}
    for item in pets:
        name, animals = item.split(":")
        animal_count = len(set(animals.split(",")))  # Using set to count unique animals
        pet_dict[name] = animal_count
    return pet_dict