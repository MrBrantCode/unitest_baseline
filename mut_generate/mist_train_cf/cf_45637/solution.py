"""
QUESTION:
Complete the function `check_dict_case(dct)` to verify whether the keys in dictionary `dct` are all lower case or all upper case. The function should return `False` for empty dictionaries and dictionaries with mixed-case keys. Additionally, it should consider numeric and special character keys as neither upper case nor lower case.
"""

def check_dict_case(dct):
    upper_case = 0
    lower_case = 0
    for key in dct:
        if key.isupper():
            upper_case += 1
        elif key.islower():
            lower_case += 1
        else:  
            return False
    return upper_case == len(dct) or lower_case == len(dct)