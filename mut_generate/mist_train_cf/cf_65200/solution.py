"""
QUESTION:
Write a function `multiply_by_index` that takes a list of integers as input and returns a new list where each element is the product of the corresponding element in the input list and its 0-indexed position. The function should handle lists of any length.
"""

def multiply_by_index(lst):
    return [num * index for index, num in enumerate(lst)]