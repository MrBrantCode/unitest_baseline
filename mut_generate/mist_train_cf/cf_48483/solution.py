"""
QUESTION:
Create a function `multiply_lists` that takes two lists as input and returns a new list containing the element-wise product of the input lists. If the input lists are not of equal length, the function should return an error message.
"""

def multiply_lists(list1, list2):
    if len(list1) != len(list2):
        return "Error: Lists are not of equal length."
    return [a*b for a, b in zip(list1, list2)]