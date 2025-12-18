"""
QUESTION:
Write a function `largest_negative` that takes an array of integers as input. The array contains only negative numbers and does not have any duplicate elements. The function should return the largest element in the array. The time complexity of the function should be O(n).
"""

def largest_negative(arr):
    largest = float('-inf')
    for num in arr:
        if num < 0 and num > largest:
            largest = num
    return largest