"""
QUESTION:
Write a function `find_second_minimum` that takes an array of integers as input and returns the second minimum element from the array without using comparison operations or sorting functions. The function should have a time complexity of O(n) and use constant space. If there's no second minimum element (i.e., all elements are the same), the function should return the same element as the minimum.
"""

def find_second_minimum(arr):
    min1 = float('inf')
    min2 = float('inf')

    for num in arr:
        if num < min1:
            min2 = min1
            min1 = num
        elif num != min1 and num < min2:
            min2 = num

    return min2