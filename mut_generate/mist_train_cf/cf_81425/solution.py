"""
QUESTION:
Write a function `min_diff(arr1, arr2)` that takes two lists of integers as input and returns the smallest absolute difference between any two elements from the individual lists. The function should return the smallest difference, without considering the order of the elements in the lists.
"""

def min_diff(arr1, arr2):
    min_difference = float('inf')
  
    for i in arr1:
        for j in arr2:
            difference = abs(i - j)
            if difference < min_difference:
                min_difference = difference
  
    return min_difference