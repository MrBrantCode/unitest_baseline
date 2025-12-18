"""
QUESTION:
Write a function `check_dict_case(dct)` that takes a dictionary as input and returns `True` if all its keys are either in lower case or upper case. If the dictionary is empty, consider it as satisfying the condition. Ensure the function correctly handles mixed case keys and dictionaries with a mix of lower and upper case keys.
"""

def check_dict_case(dct):
    if not dct:
        return True
    lower_case = sum([1 for k in dct.keys() if k.islower()])
    upper_case = sum([1 for k in dct.keys() if k.isupper()])
    return lower_case == len(dct) or upper_case == len(dct)