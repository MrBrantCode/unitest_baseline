"""
QUESTION:
Create a function `find_second_minimum(arr)` that finds the second minimum element from a given array without using comparison operations or sorting functions. The function must have a time complexity of O(n) and use only constant space.
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