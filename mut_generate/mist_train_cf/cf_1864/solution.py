"""
QUESTION:
Design a function called `longest_prime_subarray` that takes a list of positive integers as input and returns the length of the longest subarray in the list whose sum is a prime number. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def longest_prime_subarray(nums):
    """
    Returns the length of the longest subarray in the list whose sum is a prime number.

    Args:
    nums (list): A list of positive integers.

    Returns:
    int: The length of the longest subarray with a prime sum.
    """
    max_length = 0
    current_sum = 0
    left = 0
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= 2 and not is_prime(current_sum):
            current_sum -= nums[left]
            left += 1
        if is_prime(current_sum):
            max_length = max(max_length, right - left + 1)
    return max_length