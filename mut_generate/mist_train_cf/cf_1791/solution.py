"""
QUESTION:
Design a function `find_max_value` that takes an array `arr` as input and returns a tuple containing the maximum value and its index. The array may contain duplicate elements and negative values, and has a maximum length of 10^6. The function should have a time complexity of O(n), where n is the length of the array, and should break early if the maximum value found so far is greater than or equal to 100. If there are multiple maximum values, the function should return the index of the first occurrence of the maximum value.
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
        elif arr[i] == max_value:
            continue
        if max_value >= 100:
            break
    
    return (max_value, max_index)