"""
QUESTION:
Write a function `max_contiguous_sum` that takes a list of integers as input and returns the maximum sum of a contiguous subsequence. The input list represents a sequence of integers. The function should return the maximum sum of a contiguous subsequence, where a contiguous subsequence is a sequence of consecutive elements from the original sequence.
"""

def max_contiguous_sum(sequence):
    max_sum = current_sum = sequence[0]
    
    for num in sequence[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum