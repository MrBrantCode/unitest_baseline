"""
QUESTION:
Create a function `check_dict_case` that takes a dictionary `dct` as input and returns a string indicating the case of the dictionary keys. The function should return 'Lower' if all keys are in lower case, 'Upper' if all keys are in upper case, 'Number' if all keys start with a numeral, 'Special Characters' if any key contains special characters, 'Empty' if the dictionary is empty, and 'None' otherwise.
"""

def check_dict_case(dct):
    if not dct:  # if dict is empty
        return 'Empty'
    lower, upper, number, special_char = 0, 0, 0, 0  # initialize counters
    for key in dct:
        if key.islower():  # all characters are lower case
            lower += 1
        elif key.isupper():  # all characters are upper case
            upper += 1
        elif key[0].isdigit():  # begins with a digit 
            number += 1
        else:
          for ch in key:
            if not ch.isalnum():  # check for special characters
              special_char += 1
              break
    if lower == len(dct):  # all keys are lower case
        return "Lower"
    elif upper == len(dct):  # all keys are upper case
        return "Upper"
    elif number > 0:  # keys begin with numeral
        return "Number"
    elif special_char > 0:  # keys contain special characters
        return "Special Characters"
    else:
        return 'None'  # None of the above cases