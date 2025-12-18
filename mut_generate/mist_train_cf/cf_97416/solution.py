"""
QUESTION:
Write a recursive function `find_max_value` to find the maximum value and its index in a given array of integers. The function should return a tuple containing the maximum value and its index. If the maximum value appears multiple times, return the index of the first occurrence.
"""

def find_max_value(arr):
    def helper(arr, index, max_value, max_index):
        if index == len(arr):
            return max_value, max_index
        
        if max_value is None or arr[index] > max_value:
            max_value = arr[index]
            max_index = index
        
        return helper(arr, index+1, max_value, max_index)
    
    return helper(arr, 0, None, 0)