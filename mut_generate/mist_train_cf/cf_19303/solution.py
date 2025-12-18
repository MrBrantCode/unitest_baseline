"""
QUESTION:
Write a function `is_strictly_increasing` that determines if the elements of an array are in strictly increasing order, where the array may contain both positive and negative integers. The function should return True if the elements are in strictly increasing order (i.e., each element is greater than the previous one) and False otherwise.
"""

def is_strictly_increasing(arr):
    return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))