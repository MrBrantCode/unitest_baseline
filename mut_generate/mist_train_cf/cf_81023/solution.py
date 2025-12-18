"""
QUESTION:
Compute the function `compute_divergence(arr)` that takes a list of integers `arr` and returns a tuple containing the divergence between the maximum and minimum integers, the index of the maximum integer, and the index of the minimum integer. If the list is empty, return `None, None, None`. The function should handle lists with duplicate integers, negative integers, and lists of up to 10^6 elements without exceeding computational time and space constraints.
"""

def compute_divergence(arr):
    if not arr:
        return None, None, None

    apex = nadir = arr[0]
    apex_index = nadir_index = 0

    for i in range(1, len(arr)):
        if arr[i] > apex:
            apex = arr[i]
            apex_index = i
        elif arr[i] < nadir:
            nadir = arr[i]
            nadir_index = i

    divergence = apex - nadir
    return divergence, apex_index, nadir_index