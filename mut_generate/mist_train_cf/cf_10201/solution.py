"""
QUESTION:
Implement a function named `sort_array` that takes an array of integers as input and returns the array sorted in ascending order. The array can contain both positive and negative integers. You cannot use any built-in sorting functions or methods.
"""

def sort_array(arr):
    # Check if the array is empty or has only one element
    if len(arr) < 2:
        return arr

    # Find the minimum value in the array
    min_val = min(arr)

    # Find the maximum value in the array
    max_val = max(arr)

    # Create a frequency array with the range between min_val and max_val
    freq_arr = [0] * (max_val - min_val + 1)

    # Count the occurrences of each element in the array
    for num in arr:
        freq_arr[num - min_val] += 1

    # Create a new sorted array
    sorted_arr = []
    for i in range(len(freq_arr)):
        sorted_arr.extend([i + min_val] * freq_arr[i])

    return sorted_arr