"""
QUESTION:
Write a function `check_dict_case` that takes a dictionary `dct` as input. The function should return the case type of the dictionary's keys. The case type can be one of the following: all keys are in lower case ('Lower'), all keys are in upper case ('Upper'), all keys start with a number ('Number'), or all keys have an underscore as a prefix ('Underscore'). If the dictionary is empty, the function should return 'Empty'. If the dictionary's keys do not fall into any of these categories, the function should return 'None'.
"""

def check_dict_case(dct):
    if not dct:
        return 'Empty'

    cases = {'Lower': 1, 'Upper': 1, 'Number': 1, 'Underscore': 1}
    
    for key in dct:
        if key[0] == '_':
            cases['Lower'] = cases['Upper'] = cases['Number'] = 0
        elif key[0].isnumeric():
            cases['Lower'] = cases['Upper'] = cases['Underscore'] = 0
        elif key.isupper():
            cases['Lower'] = cases['Number'] = cases['Underscore'] = 0
        elif key.islower():
            cases['Upper'] = cases['Number'] = cases['Underscore'] = 0
        
        else:
            return None
            
    if cases['Lower']:
        return 'Lower'
    elif cases['Upper']:
        return 'Upper'
    elif cases['Number']:
        return 'Number'
    elif cases['Underscore']:
        return 'Underscore'