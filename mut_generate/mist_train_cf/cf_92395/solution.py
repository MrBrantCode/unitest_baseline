"""
QUESTION:
Implement a function `find_max(arr)` that finds the maximum element in an array using the sequential search algorithm. The function takes an array of integers as input, where the length of the array is between 1 and 10^6, and each element is an integer between 1 and 10^6. The function should have a time complexity of O(n) and a space complexity of O(1). If the input array is empty, the function should return None.
"""

def find_max(arr):
    if len(arr) == 0:
        return None
    
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    
    return max_element