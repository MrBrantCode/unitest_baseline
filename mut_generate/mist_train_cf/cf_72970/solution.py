"""
QUESTION:
Find a contiguous subsequence in a given binary string that sums up to a target number. The function should be named `max_binary_gap`.
"""

def max_binary_gap(N, target):
    """
    Find a contiguous subsequence in a given binary string that sums up to a target number.

    Args:
        N (str): A binary string.
        target (int): The target sum.

    Returns:
        str: A contiguous subsequence in N that sums up to target.
    """
    for length in range(len(N), 0, -1):
        for i in range(len(N) - length + 1):
            subsequence = N[i:i+length]
            if sum(int(digit) for digit in subsequence) == target:
                return subsequence
    return ""  # Return an empty string if no such subsequence is found