"""
QUESTION:
Write a function `find_largest_number(array)` that finds the largest number in the given array and its corresponding index. If multiple numbers have the same maximum value, return the index of the first occurrence. The function should have a time complexity of O(n), use only a single loop to iterate through the array, and not use any built-in array sorting or searching functions. The array will contain only positive integers.
"""

def find_largest_number(array):
    max_num = array[0]  # Initialize the maximum number with the first element of the array
    max_index = 0  # Initialize the index of the maximum number with 0

    for i in range(1, len(array)):  # Start iterating from the second element of the array
        if array[i] > max_num:  # If the current element is greater than the maximum number
            max_num = array[i]  # Update the maximum number
            max_index = i  # Update the index of the maximum number

    return max_num, max_index