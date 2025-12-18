"""
QUESTION:
Write a function `multiply_by_sum` that takes an array of positive integers as input and returns the product of each number in the array multiplied by the sum of all numbers in the array. The input array will always have at least one element and the sum of the input array will never exceed 10^9.
"""

def multiply_by_sum(arr):
    arr_sum = sum(arr)
    result = 1
    for num in arr:
        result *= num * arr_sum
    return result