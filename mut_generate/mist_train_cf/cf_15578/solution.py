"""
QUESTION:
Write a function `find_maximum` that takes a list of integers as input and returns the maximum element in the list. The function should iterate over the list only once. Analyze the time and space complexity of the function using Big O notation.
"""

def findMaximum(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val