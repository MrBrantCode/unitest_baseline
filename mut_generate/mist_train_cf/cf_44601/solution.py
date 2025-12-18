"""
QUESTION:
Create a function `raise_to_power_three` that takes a list of mixed data types as input. Return a new list with each integer item from the input list raised to the power of 3, excluding all non-integer and negative values.
"""

def raise_to_power_three(lst):
    new_lst = []
    for item in lst:
        if not isinstance(item, int):
            continue
        elif item < 0:
            continue
        else:
            new_lst.append(item ** 3)
    return new_lst