"""
QUESTION:
Create a function named `get_value` that takes a dictionary and a list as input, along with an integer. The function should return the dictionary value corresponding to the given integer if the integer is present in the list. Otherwise, it should return `None`.
"""

def entance(dictionary, lst, integer):
    if integer in lst:
        return dictionary.get(integer)
    else:
        return None