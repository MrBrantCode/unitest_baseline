"""
QUESTION:
Create a function `transform_to_dict` that takes a list of mixed data types as input and returns a dictionary. The keys of the dictionary should be the elements of the list. If a key is a string, its corresponding value should be a list `[True, length of the string]`. If a key is a number, its corresponding value should be a list `[True, square of the number]`. The function should handle both string and integer types, and the input list can contain any number of elements of each type.
"""

def transform_to_dict(lst):
    dictn = {}
    for element in lst:
        if type(element) == str:
            dictn[element] = [True, len(element)]
        elif type(element) == int:
            dictn[element] = [True, element * element]
    return dictn