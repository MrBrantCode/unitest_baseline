"""
QUESTION:
Implement a function named `sort_array` that sorts an array of integers in ascending order without using any built-in sorting functions or methods. The array can contain both positive and negative integers. The function should return the sorted array. The input array is guaranteed to be a list of integers, but can be empty or contain duplicate values.
"""

def sort_array(arr):
    if len(arr) < 2:
        return arr

    min_val = min(arr)
    max_val = max(arr)

    freq_arr = [0] * (max_val - min_val + 1)

    for num in arr:
        freq_arr[num - min_val] += 1

    sorted_arr = []
    for i in range(len(freq_arr)):
        sorted_arr.extend([i + min_val] * freq_arr[i])

    return sorted_arr