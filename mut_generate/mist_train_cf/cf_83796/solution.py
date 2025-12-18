"""
QUESTION:
Write a function named `check_dict_case` that takes one parameter, `dct`, which is a dictionary. The function should check if all keys in the dictionary are either completely lower case, completely upper case, or start with a numeric digit. It should return 'Lower' if all keys are completely lower case, 'Upper' if all keys are completely upper case, 'Number' if all keys start with a numeric digit, 'None' if the keys do not meet any of the above conditions, and 'Empty' if the dictionary is empty.
"""

def check_dict_case(dct):
    if not dct:
        return 'Empty'
    lower_case = all([k.islower() for k in dct.keys()])
    upper_case = all([k.isupper() for k in dct.keys()])
    number_case = all([k[0].isdigit() for k in dct.keys()])
    if lower_case:
        return 'Lower'
    elif upper_case:
        return 'Upper'
    elif number_case:
        return 'Number'
    else:
        return 'None'