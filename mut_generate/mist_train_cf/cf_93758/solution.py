"""
QUESTION:
Write a function `find_max_indices` that takes an array of integers as input and returns the indices of all occurrences of the maximum number in ascending order. If the maximum number appears only once, return a list with a single index. If the array does not contain the maximum number (which will never be the case), return an empty list. The time complexity of the solution should be O(n), where n is the size of the input array.
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