"""
QUESTION:
Write a function `smallest_subarray` that finds the smallest subarray in a given array with a sum equal to `S` and an average equal to `A`. If multiple subarrays meet these conditions, return the first one. The function should have a time complexity of O(n), where n is the size of the array. The function should take three parameters: the input array `arr`, the required sum `S`, and the required average `A`.
"""

def smallest_subarray(arr, S, A):
    """
    This function finds the smallest subarray in a given array with a sum equal to S and an average equal to A.
    
    Parameters:
    arr (list): The input array.
    S (int): The required sum.
    A (float): The required average.
    
    Returns:
    list: The smallest subarray that meets the conditions.
    """
    
    window_start, current_sum = 0, 0
    smallest_len = float('inf')
    smallest_subarray = None

    for window_end in range(len(arr)):
        current_sum += arr[window_end]

        while current_sum >= S:
            if current_sum == S and (current_sum / (window_end - window_start + 1) == A):
                if window_end - window_start + 1 < smallest_len:
                    smallest_len = window_end - window_start + 1
                    smallest_subarray = arr[window_start:window_end+1]
            current_sum -= arr[window_start]
            window_start += 1
    return smallest_subarray