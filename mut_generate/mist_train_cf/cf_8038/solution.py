"""
QUESTION:
Write a function `remove_element` that takes an array `arr` and an integer `index` as input. The function should modify the array in place by removing the element at the specified `index` and shifting the remaining elements one position to the left. If the `index` is out of bounds or the array is empty, return the original array unchanged. Do not use any built-in functions or methods that directly remove an element from an array, and ensure a time complexity of O(n), where n is the length of the array.
"""

def remove_element(arr, index):
    if index < 0 or index >= len(arr):
        return arr
    
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i+1]
    
    arr.pop()
    return arr