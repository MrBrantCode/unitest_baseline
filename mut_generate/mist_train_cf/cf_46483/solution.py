"""
QUESTION:
Implement a function `reverse_dict_values` that takes a dictionary where values are lists, and returns a new dictionary with the same keys and values in reverse order. 

Implement another function `are_mirror_images` that checks if two dictionaries with list values are mirror images of each other, meaning their corresponding list values contain the same elements in reverse order. The function should return True if the dictionaries are mirror images and False otherwise.
"""

def reverse_dict_values(input_dict):
    """Reverses the array or list values in a dictionary."""
    result_dict = {}
    for key, value in input_dict.items():
        result_dict[key] = value[::-1]
    return result_dict

def are_mirror_images(dict1, dict2):
    """Checks if two dictionaries have mirror image value arrays or lists."""
    for key in dict1.keys():
        if dict1[key] != dict2[key][::-1]:
            return False
    return True