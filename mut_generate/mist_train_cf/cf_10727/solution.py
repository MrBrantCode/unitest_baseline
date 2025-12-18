"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers as input and returns a new array containing the same elements but with no duplicates, without modifying the original array.
"""

def remove_duplicates(input_array):
    unique_array = []
    for num in input_array:
        if num not in unique_array:
            unique_array.append(num)
    return unique_array