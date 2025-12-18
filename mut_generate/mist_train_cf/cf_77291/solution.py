"""
QUESTION:
Write a function `max_elements_subarray(arr, total)` that finds the longest subarray within the given array `arr` whose elements add up to the given number `total`. The function should return the longest subarray that meets this condition.
"""

def max_elements_subarray(arr, total):
    max_length = None
    max_subarray = None
        
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub_arr = arr[i:j+1]  # Include j in the subarray
            if sum(sub_arr) == total:
                if max_length is None or len(sub_arr) > max_length:
                    max_length = len(sub_arr)
                    max_subarray = sub_arr
    return max_subarray