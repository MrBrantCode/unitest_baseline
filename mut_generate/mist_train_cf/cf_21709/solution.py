"""
QUESTION:
Write a function `find_max_positive(arr)` that takes an array of numbers as input and returns the index of the maximum positive number. If there are multiple positive numbers with the same maximum value, return the index of the first occurrence. If there are no positive numbers in the array, return -1. The time complexity of the function should be O(n), where n is the length of the array.
"""

def find_max_positive(arr):
    max_positive = -1
    max_index = -1
    
    for i, num in enumerate(arr):
        if num > 0 and (max_positive == -1 or num > max_positive):
            max_positive = num
            max_index = i
    
    return max_index