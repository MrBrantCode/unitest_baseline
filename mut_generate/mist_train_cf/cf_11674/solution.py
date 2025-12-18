"""
QUESTION:
Given an array of positive integers, write a function `multiply_and_sort` that returns an array with the elements multiplied by three and sorted in descending order.
"""

def multiply_and_sort(arr):
    result = []
    for num in arr:
        result.append(num * 3)
    result.sort(reverse=True)
    return result