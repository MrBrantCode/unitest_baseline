"""
QUESTION:
Create a function named `cube_nested_list` that takes a list of numbers as input, which can be nested. The function should calculate the cube of each number in the list while maintaining the original structure of the nested lists.
"""

def cube_nested_list(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.append(cube_nested_list(i))
        else:
            result.append(i**3)
    return result