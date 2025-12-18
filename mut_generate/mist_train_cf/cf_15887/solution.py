"""
QUESTION:
Find a function `find_prime_pair` that takes an array of positive integers and a target sum as input. The function should return the two smallest prime numbers in the array that add up to the target sum and have a prime product. If no such pair exists, return None.
"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime_pair(nums, target):
    """
    Find the two smallest prime numbers in the array that add up to the target sum and have a prime product.

    Args:
    nums (list): A list of positive integers.
    target (int): The target sum.

    Returns:
    list: A list of two prime numbers that satisfy the conditions, or None if no such pair exists.
    """
    nums.sort()
    prime_nums = [num for num in nums if is_prime(num)]
    
    for i in range(len(prime_nums)):
        for j in range(i + 1, len(prime_nums)):
            if prime_nums[i] + prime_nums[j] == target and is_prime(prime_nums[i] * prime_nums[j]):
                return [prime_nums[i], prime_nums[j]]
    
    return None