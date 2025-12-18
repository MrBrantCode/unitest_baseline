"""
QUESTION:
Create a function named check_dict_case that takes a dictionary as input. The function should return True if all keys in the dictionary are either exclusively lower case or upper case, and False otherwise. If the input dictionary is empty, the function should also return False.
"""

def check_dict_case(dct):
    if not dct:
        return False
    lower_case = sum([k.islower() for k in dct.keys()])
    upper_case = sum([k.isupper() for k in dct.keys()])
    return lower_case == len(dct) or upper_case == len(dct)