"""
QUESTION:
Write a function `calculate_mean` that takes a list of integers as input and returns the mean of the numbers in the list. The list will contain integers within the range of 1-5 (inclusive). The list will not be empty.
"""

def calculate_mean(lst):
    total = 0
    for num in lst:
        total += num
    return total / len(lst)