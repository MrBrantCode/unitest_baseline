"""
QUESTION:
Create a function named `add_integer_to_list` that takes a list of integers and an integer as arguments. The function should add the given integer to each element of the list and return the new list. The time complexity of the function should be O(n), where n is the length of the list.
"""

def add_integer_to_list(lst, integer):
    return [element + integer for element in lst]