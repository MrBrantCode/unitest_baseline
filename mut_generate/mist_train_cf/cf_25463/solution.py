"""
QUESTION:
Create a function named "product" that takes an array of numbers as input and returns the total product of all numbers in the array. The function should be able to handle arrays with any number of elements.
"""

def product(arr):
    result = 1
    for num in arr:
        result *= num
    return result