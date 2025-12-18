"""
QUESTION:
Write a function `check_dict_case` that takes a dictionary `dct` as input and returns `True` if all keys in the dictionary are either all in lower case or all in upper case. The function should return `False` if the dictionary is empty, contains keys with mixed case, or contains non-alphabetical characters. Keys are considered to be in lower case or upper case only if the entire key is in that case.
"""

def check_dict_case(dct):
    if len(dct) == 0:
        return False
        
    lower_case = sum(k.islower() for k in dct.keys())
    upper_case = sum(k.isupper() for k in dct.keys())
    
    # All keys are either in lower case, upper case or a mix
    mix_case = any(not k.isupper() and not k.islower() for k in dct.keys())

    # if all keys are either lower, upper or there is a mix then return False, otherwise True
    return not (lower_case == len(dct) or upper_case == len(dct) or mix_case)