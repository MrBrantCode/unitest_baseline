"""
QUESTION:
Write a function `optimize_set` that takes a list of integers as input and returns the highest total sum that can be achieved by selecting a combination of values from the input list. The function should only consider positive integers in the input list.
"""

def optimize_set(values):
    return sum(value for value in values if value > 0)