"""
QUESTION:
Implement a function `check_dict_case(d)` that examines if all keys in a given dictionary `d` comprise only lower case or only upper case letters. The function should return `False` for empty dictionaries.
"""

def check_dict_case(d):
    if not d: 
        return False 

    lower = 0
    upper = 0

    for key in d:
        if key.islower():
            lower += 1
        elif key.isupper():
            upper += 1   
        else:
            return False

    if lower == len(d) or upper == len(d):
        return True
    else:
        return False