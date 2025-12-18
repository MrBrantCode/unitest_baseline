"""
QUESTION:
Find a contiguous subsequence of binary numbers in a given sequence that sums up to a target sum. The function should be named `find_subsequence` and take two parameters: a list of binary numbers and the target sum. The function should return the subsequence if found, or None otherwise.
"""

def find_subsequence(binary_numbers, target_sum):
    """
    Finds a contiguous subsequence of binary numbers in a given sequence that sums up to a target sum.

    Args:
        binary_numbers (list): A list of binary numbers.
        target_sum (int): The target sum.

    Returns:
        list or None: The subsequence if found, or None otherwise.
    """
    left = 0
    current_sum = 0
    for right in range(len(binary_numbers)):
        current_sum += binary_numbers[right]
        while current_sum > target_sum and left <= right:
            current_sum -= binary_numbers[left]
            left += 1
        if current_sum == target_sum:
            return binary_numbers[left:right + 1]
    return None