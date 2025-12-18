"""
QUESTION:
Complete the function `check_dict_case(dictionary)` to check if all keys in the given dictionary are either all lower case or all upper case. The function should return `False` for empty dictionaries.
"""

def check_dict_case(dictionary):
    return dictionary and len(set(k.islower() or k.isupper() for k in dictionary)) == 1