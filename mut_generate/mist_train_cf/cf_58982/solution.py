"""
QUESTION:
Create a function named `check_dict_case` that takes a dictionary as input and returns True if all keys in the dictionary are either all lower case or all upper case, and False otherwise. The function should return False for an empty dictionary.
"""

def check_dict_case(dct):
    if not dct:
        return False
    lower_case = sum([k.islower() for k in dct.keys()])
    upper_case = sum([k.isupper() for k in dct.keys()])
    return lower_case == len(dct) or upper_case == len(dct)