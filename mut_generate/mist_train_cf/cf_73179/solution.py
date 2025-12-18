"""
QUESTION:
Create a recursive function `find_min` that takes a list of integers as input and returns the smallest integer in the list. The function should be able to handle lists of any length and should not use any built-in functions for finding the minimum, except for the built-in `min` function to compare two numbers.
"""

def find_min(input_list):
    # Base case: if list only contains one element, return that element
    if len(input_list) == 1:
        return input_list[0]
    else:
        # Recursive call: compare the first element with the minimum of the rest
        return min(input_list[0], find_min(input_list[1:]))