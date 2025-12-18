"""
QUESTION:
Create a function called `multiply_and_sort` that takes an array of positive integers as input. The function should return a new array containing the input elements multiplied by three and sorted in descending order.
"""

def multiply_and_sort(arr):
    result = []
    for num in arr:
        result.append(num * 3)
    result.sort(reverse=True)
    return result