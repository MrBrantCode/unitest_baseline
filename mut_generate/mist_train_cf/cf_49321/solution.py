"""
QUESTION:
Write a function `check_dict_case(dct)` that takes a dictionary as input and returns `True` if all keys are non-empty, exclusively contain letters, and are either entirely in uppercase or lowercase. If the dictionary is empty or any of these conditions are not met, the function should return `False`.
"""

def check_dict_case(dct):
    if not dct:    # if dictionary is empty, return False
        return False
    # To count lowercase and uppercase key entries
    lower_case = sum([k.islower() for k in dct.keys()])
    upper_case = sum([k.isupper() for k in dct.keys()])
    # Check if all characters in the keys are alphabets
    is_alpha = sum([k.isalpha() for k in dct.keys()])
    # Only return True if all keys are alphanumeric and either all in uppercase or all in lowercase
    return (is_alpha == len(dct)) and (lower_case == len(dct) or upper_case == len(dct))