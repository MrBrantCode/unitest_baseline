"""
QUESTION:
Write a function `max_subarray_sum(sequence)` that takes in a list of integers `sequence` and returns the sum of the contiguous subarray with the largest sum. The function must have a time complexity of O(n), where n is the number of elements in the sequence.
"""

def max_subarray_sum(sequence):
    max_ending_here = max_so_far = sequence[0]  
    for x in sequence[1:]:  
        max_ending_here = max(x, max_ending_here + x)  
        max_so_far = max(max_so_far, max_ending_here)  
    return max_so_far