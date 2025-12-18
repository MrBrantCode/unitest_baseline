"""
QUESTION:
Create a function `filter_list` that takes a list of numbers and a given number as input, and returns a new list containing only the numbers from the original list that are greater than the given number.
"""

def filter_list(lst, given_number):
    return [num for num in lst if num > given_number]