"""
QUESTION:
Write a function named `check_dict_case` that checks if all keys in a given dictionary are either all lower case or all upper case. The function should return False for empty dictionaries.
"""

def check_dict_case(dct):
    if not dct:
        return False
    lower_case = sum([k.islower() for k in dct.keys()])
    upper_case = sum([k.isupper() for k in dct.keys()])
    return lower_case == len(dct) or upper_case == len(dct)