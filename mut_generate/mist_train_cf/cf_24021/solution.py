"""
QUESTION:
Create a function called `group_pets` that takes a list of strings, where each string contains a name and the number of pet animals owned, separated by a space and the type of pet. The function should return a dictionary where the keys are the names and the values are the corresponding number of pet animals owned. The list of strings will be in the format ["name number type", "name number type", ...] and the number of pet animals will always be an integer.
"""

def group_pets(pets_list):
    """
    This function takes a list of strings where each string contains a name and the number of pet animals owned,
    separated by a space and the type of pet. It returns a dictionary where the keys are the names and the values
    are the corresponding number of pet animals owned.

    Args:
        pets_list (list): A list of strings containing name, number of pets, and type of pet.

    Returns:
        dict: A dictionary with names as keys and number of pets as values.
    """
    pets_dict = {}
    for pet in pets_list:
        name, number, _ = pet.split()
        pets_dict[name] = int(number)
    return pets_dict