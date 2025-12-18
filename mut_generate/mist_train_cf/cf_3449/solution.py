"""
QUESTION:
Write a function named `count_prime_pairs` that takes an array of positive integers as input and returns the count of pairs whose absolute difference is a prime number. The function should have a time complexity of O(n^2) and use only constant space, without modifying the input array.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_prime_pairs(nums):
    """
    Count the pairs in the array whose absolute difference is a prime number.

    Args:
        nums (list): A list of positive integers.

    Returns:
        int: The count of pairs whose absolute difference is a prime number.
    """
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            diff = abs(nums[i] - nums[j])
            if is_prime(diff):
                count += 1
    return count