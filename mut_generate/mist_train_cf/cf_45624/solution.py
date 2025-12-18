"""
QUESTION:
Create a function `check_dict_case` that checks if the keys in a given dictionary are either uniformly lower or upper case, and also checks if the values inside the dictionary are uniformly lower or upper case. The function should return False if the dictionary is empty.
"""

def check_dict_case(dct):
    if not dct:
        return False
    
    # Checks for all lowercase or uppercase keys.
    all_lower_keys = all(k.islower() for k in dct.keys())
    all_upper_keys = all(k.isupper() for k in dct.keys())
    if not (all_lower_keys or all_upper_keys):
        return False

    # Checks for all lowercase or uppercase values.
    all_lower_values = all(str(v).islower() for v in dct.values())
    all_upper_values = all(str(v).isupper() for v in dct.values())
    if not (all_lower_values or all_upper_values):
        return False

    return True