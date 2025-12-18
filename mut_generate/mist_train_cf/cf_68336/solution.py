"""
QUESTION:
Create a function named `sum_array` that takes an array of integers as input and returns the sum of all elements in the array using a for loop. The function should not use any built-in sum functions.
"""

def sum_array(arr):
    total = 0
    for i in arr:
        total += i
    return total