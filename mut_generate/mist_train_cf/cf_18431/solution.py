"""
QUESTION:
Write a function `find_largest_sum(arr)` that takes an array of integers as input and returns a list of the two elements with the largest sum. If there are multiple pairs with the same largest sum, return the pair with the smallest element. The function should run in linear time, i.e., O(n), where n is the length of the input array.
"""

def find_largest_sum(arr):
    max1 = max(arr[0], arr[1])
    max2 = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]

    return [max1, max2]