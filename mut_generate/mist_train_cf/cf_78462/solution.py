"""
QUESTION:
Create a function called check_dict_case that takes a dictionary as input. The function should check if all keys in the dictionary are either entirely in lower case, entirely in upper case, or start with a numerical digit. It should return 'None' if the dictionary contains a mix of these cases, 'Lower' if all keys are in lower case, 'Upper' if all keys are in upper case, 'Number' if all keys start with a numerical digit, and 'Empty' if the dictionary is empty.
"""

def check_dict_case(dct):
    if not dct:
        return 'Empty'
    lower_case = sum([k == k.lower() for k in dct.keys()])
    upper_case = sum([k == k.upper() for k in dct.keys()])
    number_case = sum([k[0].isdigit() for k in dct.keys()])
    if lower_case == len(dct):
        return 'Lower'
    elif upper_case == len(dct):
        return 'Upper'
    elif number_case == len(dct):
        return 'Number'
    else:
        return 'None'