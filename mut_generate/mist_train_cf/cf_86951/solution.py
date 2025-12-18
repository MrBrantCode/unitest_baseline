"""
QUESTION:
Write a function named `find_max` that takes a list of integers `arr` as input and returns the index of the first occurrence of the maximum value in the list. The function should not use any built-in array functions, sorting algorithms, or loops, and instead should use recursion or functional programming techniques.
"""

def entance(arr):
    def find_max_helper(arr, current_max, current_index, max_index):
        if current_index == len(arr):
            return max_index

        if arr[current_index] > current_max:
            return find_max_helper(arr, arr[current_index], current_index + 1, current_index)
        else:
            return find_max_helper(arr, current_max, current_index + 1, max_index)

    return find_max_helper(arr, arr[0], 0, 0)