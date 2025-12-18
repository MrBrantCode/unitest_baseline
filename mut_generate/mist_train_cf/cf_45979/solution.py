"""
QUESTION:
Write a function `can_arrange(arr)` that takes an array of distinct integers as input and returns a dictionary containing the index of the first element that is smaller than its predecessor, the index of the smallest subsequent element that can replace it to correct the sequence, and the total number of swaps required to correct the sequence. If the array is already sorted, return {'index': -1, 'swap_with': -1, 'total_swaps': 0}.
"""

def entrance(arr):
    n = len(arr)
    total_swaps = 0
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            swap_index = i
            # Find next substitute
            while swap_index < n and arr[swap_index] < arr[i-1]:
                swap_index += 1
            # Decrease the swap_index by 1 as it has been increased in the while loop
            swap_index -= 1
            # Swap elements
            arr[i-1], arr[swap_index] = arr[swap_index], arr[i-1]
            # increment total swaps
            total_swaps += 1
            # No need to continue the loop as only 1 operation is allowed.
            return {'index': i-1, 'swap_with': swap_index, 'total_swaps': total_swaps}
    return {'index': -1, 'swap_with': -1, 'total_swaps': 0}