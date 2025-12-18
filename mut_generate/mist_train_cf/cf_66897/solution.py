"""
QUESTION:
Write a function named `sort_decimals` that takes a list of decimal numbers as input and returns a new list containing the same numbers in descending order. The function should handle duplicate decimal numbers and place them next to each other in the output list.
"""

def entrance(dec_list):
    sorted_list = sorted(dec_list, reverse=True)
    return sorted_list