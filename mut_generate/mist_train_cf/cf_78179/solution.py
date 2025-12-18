"""
QUESTION:
Implement a function `sum_of_nums` that takes a list of integers as input and returns their sum. The function should handle cases where the input list is empty or contains non-numeric characters, and return an error message in such cases. The function should also validate that the input is a list and return an error message if it is not.
"""

def entrance(input_list):
    if not isinstance(input_list, list):
        return "Input should be a List"
    total = 0
    for i in input_list:
        if isinstance(i, int):
            total += i
        else:
            return "List should only contain integers"
    return total