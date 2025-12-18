"""
QUESTION:
Write a function called `find_max` that takes an array of integers as input and returns the index of the first occurrence of the maximum value in the array without using any built-in array functions, sorting algorithms, loops, or recursion with more than one recursive call per function.
"""

def find_max(arr):
    def find_max_helper(arr, current_max, current_index, max_index):
        if current_index == len(arr):
            return max_index
        if arr[current_index] > current_max:
            return find_max_helper(arr, arr[current_index], current_index + 1, current_index)
        else:
            return find_max_helper(arr, current_max, current_index + 1, max_index)
    return find_max_helper(arr, arr[0], 0, 0)