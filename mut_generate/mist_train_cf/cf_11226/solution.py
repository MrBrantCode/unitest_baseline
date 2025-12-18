"""
QUESTION:
Write a function named `sum_of_squares` that takes an array as input and returns the sum of the squares of its integer elements. The function should ignore non-integer elements in the array.
"""

def sum_of_squares(arr):
    total_sum = 0
    for num in arr:
        if isinstance(num, int):
            total_sum += num**2
    return total_sum