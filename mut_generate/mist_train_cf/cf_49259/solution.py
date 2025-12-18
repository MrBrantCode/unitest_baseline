"""
QUESTION:
Write a function `check_dict_case` that takes a dictionary `dct` as input. The function should return `True` if all keys in the dictionary are either all lower case or all upper case, and `False` otherwise. If the dictionary is empty, the function should return `False`.
"""

def check_dict_case(dct):
    if not dct:
        return False
    lower_case = sum([k.islower() for k in dct.keys()])
    upper_case = sum([k.isupper() for k in dct.keys()])
    return (lower_case == len(dct) or upper_case == len(dct))