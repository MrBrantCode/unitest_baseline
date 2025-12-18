"""
QUESTION:
Write a function `find_max_value` that takes a list of integers as input and returns a tuple containing the maximum value and its index in the list. The function should have a time complexity of O(n), where n is the length of the list, and should handle lists with up to 10^6 elements, including negative values and duplicates. The function should also break early and return the maximum value and its index if the maximum value is greater than or equal to 100. If there are multiple maximum values, the function should return the index of the first occurrence.
"""

def find_max_value(arr):
    n = len(arr)
    
    if n == 0:
        return None
    
    max_value = arr[0]
    max_index = 0
    
    for i in range(1, n):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
        if max_value >= 100:
            break
    
    return (max_value, max_index)