"""
QUESTION:
Write a function `convert_range_to_odd_list` that takes a range as input and returns a list of odd numbers from the range in descending order. The list must only contain unique elements and should be sorted in descending order.
"""

def convert_range_to_odd_list(input_range):
    return sorted([num for num in input_range if num % 2 != 0], reverse=True)