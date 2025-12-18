"""
QUESTION:
Write a function named `reverse_array` that takes an array of integers as input and reverses the array in-place, i.e., it modifies the original array without creating a new one. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array. The array elements are integers between 1 and 10^9 (inclusive), and n is a positive integer not exceeding 10^6.
"""

def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    return arr