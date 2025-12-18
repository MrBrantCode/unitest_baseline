"""
QUESTION:
Write a function named `multiplication_outcome` that takes a list of integers as input and returns the product of all elements in the list. The function should initialize a variable to hold the running product, iterate through each number in the list, and multiply the running product by the current number.
"""

def multiplication_outcome(arr):
    product = 1
    for i in arr:
        product *= i
    return product