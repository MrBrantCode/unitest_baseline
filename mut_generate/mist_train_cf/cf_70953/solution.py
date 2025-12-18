"""
QUESTION:
Create a function called `group_by_length_and_sort` that takes a list as input and returns a dictionary. The function should group the strings in the list by their lengths and sort each group in alphabetical order. It should ignore any non-string elements in the list and handle duplicate strings by placing them in their respective groups.
"""

def group_by_length_and_sort(lst):
    result = {}
    for i in lst:
        if isinstance(i, str):
            if len(i) not in result:
                result[len(i)] = [i]
            else:
                result[len(i)].append(i)
    for key in result.keys():
        result[key] = sorted(result[key])
    return result