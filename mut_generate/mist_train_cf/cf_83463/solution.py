"""
QUESTION:
Write a function `process_array` that takes an array of integers as input, adds 10 to each value, and returns a new array containing only the resulting values that are odd.
"""

def process_array(arr):
    result = []
    for num in arr:
        num += 10
        if num % 2 != 0:
            result.append(num)
    return result