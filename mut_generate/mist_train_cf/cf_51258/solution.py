"""
QUESTION:
Write a function `nearest_integer` that takes a list of integers `lst` and a target integer `target` as input, and returns the integer in the list that is closest to the target value. If there are multiple integers with the same minimum distance to the target, return the smaller one. The function should also handle the following restrictions:

- If the input list is empty, return an error message.
- If the input list contains non-integer values, return an error message.
"""

def find_nearest_integer(lst, target):
    if len(lst) == 0:
        return "Error: The list cannot be empty."
    for i in lst:
        if type(i) != int:
            return "Error: The list should contain only integers."
    lst = sorted(lst, key=lambda x: (abs(x - target), x))
    return lst[0]