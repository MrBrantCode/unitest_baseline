"""
QUESTION:
Write a function named `max_product` that finds the maximum product of two numbers in an array containing both positive and negative integers. The function should take one parameter, an array of integers, and return the maximum product of two numbers in the array. If the array has less than two elements, the function should return `None`.
"""

def max_product(arr):
    if len(arr) < 2:
        return None
    
    max_product = arr[0] * arr[1]
    
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] * arr[j] > max_product:
                max_product = arr[i] * arr[j]
    
    return max_product