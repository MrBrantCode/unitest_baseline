"""
QUESTION:
Write a function named `compare_numbers` that takes a list of integers as input and returns a tuple containing the largest and smallest numbers in the list. If the input list is empty, the function should return the string "List is empty."
"""

def compare_numbers(lst):
    if len(lst) == 0:
        return "List is empty."
    else:
        maximum = max(lst)
        minimum = min(lst)
        return maximum, minimum