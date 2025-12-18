"""
QUESTION:
Write a function `find_max_indices` that takes an array of integers as input and returns a list of indices of the maximum number in the array. If the maximum number appears multiple times, return all its indices in ascending order. If the maximum number does not appear more than once or does not exist in the array, return an empty list. The function should be able to handle arrays of any size and have a time complexity of O(n), where n is the size of the input array.
"""

def find_max_indices(arr):
    max_num = float('-inf')
    max_indices = []
    
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
            max_indices = [i]
        elif arr[i] == max_num:
            max_indices.append(i)
    
    return max_indices