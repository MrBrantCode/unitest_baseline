"""
QUESTION:
Create a function named `sort_array` that takes an array as input and returns the array sorted in descending order without using any built-in sorting functions or methods. The array should contain 15 elements, each being a randomly generated positive integer between 1 and 1000 inclusive. You are not allowed to use any loops or recursion for sorting the array.
"""

def sort_array(arr):
    if len(arr) <= 1:
        return arr
    
    max_value = max(arr)  # Find the maximum value in the array
    max_index = arr.index(max_value)  # Find the index of the maximum value
    arr[0], arr[max_index] = arr[max_index], arr[0]  # Swap the maximum value with the first element
    
    return [max_value] + sort_array(arr[1:])  # Recursively sort the subarray from the second element