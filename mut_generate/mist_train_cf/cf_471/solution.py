"""
QUESTION:
Write a function `absolute_max_index` that takes in an array of integers and returns the index of the first occurrence of the absolute maximum element. The function should have a time complexity of O(n), where n is the length of the input array, and should use only constant space. Assume the input array is non-empty.
"""

def absolute_max_index(arr):
    max_index = 0
    max_value = abs(arr[0])
    
    for i in range(1, len(arr)):
        if abs(arr[i]) > max_value:
            max_index = i
            max_value = abs(arr[i])
    
    return max_index