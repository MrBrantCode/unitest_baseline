"""
QUESTION:
Find a contiguous subsequence of binary digits within a given sequence that adds up to a specific target sum. The function `find_subsequence` should take two parameters: a string of binary digits and a target sum. The function should return the starting and ending indices of the subsequence. If no such subsequence exists, return -1.
"""

def find_subsequence(sequence, target_sum):
    """
    Find a contiguous subsequence of binary digits within a given sequence that adds up to a specific target sum.

    Args:
        sequence (str): A string of binary digits.
        target_sum (int): The target sum.

    Returns:
        tuple: The starting and ending indices of the subsequence. If no such subsequence exists, return -1.
    """
    window_sum = 0
    left = 0
    for right in range(len(sequence)):
        window_sum += int(sequence[right])
        while window_sum > target_sum and left <= right:
            window_sum -= int(sequence[left])
            left += 1
        if window_sum == target_sum:
            return left, right
    return -1