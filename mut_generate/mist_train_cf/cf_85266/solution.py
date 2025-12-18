"""
QUESTION:
Write a function `multiply_nested_array` that takes an array of integers and nested arrays as input and returns the product of all integers in the array, regardless of their nesting level. The input array can contain both positive and negative integers.
"""

def multiply_nested_array(arr):
    result = 1
    for num in arr:
        if isinstance(num, list):
            result *= multiply_nested_array(num)
        else:
            result *= num
    return result