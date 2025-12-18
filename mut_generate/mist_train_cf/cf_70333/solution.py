"""
QUESTION:
Create a function `create_nested_dict(names)` that takes a list of names as input and returns a nested dictionary where the outer dictionary has keys representing the first letter of the names and the inner dictionaries store the names with their frequency count. The function should be able to handle duplicate names in the input list and update their frequency count accordingly.
"""

def entrance(names):
    result = {}
    for name in names:
        first_letter = name[0]
        if first_letter in result:
            if name in result[first_letter]:
                result[first_letter][name] += 1
            else:
                result[first_letter][name] = 1
        else:
            result[first_letter] = {name: 1}
    return result