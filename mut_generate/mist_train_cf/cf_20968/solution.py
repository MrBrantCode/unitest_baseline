"""
QUESTION:
Create a function named `remove_odd_numbers` that takes a list of integers as input and returns the modified list with all odd numbers removed. The input list can contain both positive and negative integers, as well as zero.
"""

def remove_odd_numbers(lst):
    return [num for num in lst if num % 2 == 0]