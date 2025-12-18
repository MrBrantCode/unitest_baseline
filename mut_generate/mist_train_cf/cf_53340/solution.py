"""
QUESTION:
Write a function named max_sum_contiguous that takes a list of integers as input and returns the largest sum of any four contiguous numbers in the list. The function should work for lists containing both positive and negative integers, and the list will have at least four elements.
"""

def max_sum_contiguous(lst):
    # Check the size of the list
    n = len(lst)

    # Initialize max_sum variable with lowest value
    max_sum = float("-inf")

    # nested loop to check all possible contiguous subsequence of four elements
    for i in range(n - 3):
        current_sum = sum(lst[i:i+4])
        if current_sum > max_sum:
            max_sum = current_sum
    # return max sum
    return max_sum