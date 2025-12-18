"""
QUESTION:
Create a function named `get_value` that takes a dictionary, a list, and an integer as parameters. The function should return the value from the dictionary corresponding to the given integer if it exists in the list; otherwise, it should return None.
"""

def get_value(dictionary, lst, integer):
    if integer in lst:
        return dictionary.get(integer)
    else:
        return None