"""
QUESTION:
Write a function `sort_animal_array` that takes a list of animal names as input, converts all the elements to uppercase, sorts them by length in ascending order, and when lengths match, sorts them alphabetically. The function should return the sorted list of animal names.
"""

def sort_animal_array(animal_arr):
    """
    This function takes a list of animal names, converts them to uppercase, 
    sorts them by length in ascending order, and when lengths match, 
    sorts them alphabetically.

    Args:
        animal_arr (list): A list of animal names.

    Returns:
        list: The sorted list of animal names.
    """
    # Convert all the elements in the array to uppercase
    animal_arr = [animal.upper() for animal in animal_arr]

    # Sort the array elements by length and then alphabetically
    animal_arr = sorted(animal_arr, key=lambda animal: (len(animal), animal))

    return animal_arr