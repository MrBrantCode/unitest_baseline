"""
QUESTION:
Write a function named `problem` that takes an array of four distinct integers as input. The function should calculate the product of all integers in the array and then subtract 12 from the result. If the array contains any duplicate values, the function should return -1.
"""

def problem(arr):
    if len(arr) != len(set(arr)):  
        return -1

    product = 1
    subtract_value = 12
    for value in arr:
        product *= value

    return product - subtract_value