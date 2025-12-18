"""
QUESTION:
Write a function called `multiply` that takes an array of integers as input, multiplies all the numbers in the array together, and returns the result as a floating-point number. The function should be able to handle arrays containing negative numbers.
"""

def multiply(arr):
    product = 1
    for num in arr:
        product *= num
    return float(product)