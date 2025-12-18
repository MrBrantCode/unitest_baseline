"""
QUESTION:
Reverse a given array's elements in-place and calculate the sum of all the elements in the reversed array. The function should be named `reverse_array` and take an array of integers as input. The input array will contain up to 10^6 elements, all of which will be integers between -10^6 and 10^6 (inclusive). The solution should have a time complexity of O(n) and a space complexity of O(1). The function should return the reversed array and the sum of its elements.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    total = 0

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        total += arr[start] + arr[end]
        start += 1
        end -= 1

    if start == end:
        total += arr[start]

    return arr, total