"""
QUESTION:
Create a function named `cumulative_array` that takes an array of integers and a list of indexes as input and returns a new array containing the cumulative totals of the original array elements corresponding to the provided indexes. The function should correctly handle repeated indexes, accumulating the current total for each index. The input array and list of indexes are interactively input line by line, with each integer in a new line, and ended with an empty input (newline).
"""

def cumulative_array(arr, index):
    cumul_arr = [0] * len(index)
    for i, ind in enumerate(index):
        cumul_arr[i] += cumul_arr[i-1] + arr[ind] if i != 0 else arr[ind]
    return cumul_arr