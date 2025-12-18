"""
QUESTION:
Write a function `removeDuplicatesAndSort` that takes an array of integers as input, removes all non-prime numbers and duplicates, and returns a sorted array in ascending order. If the input array does not contain any prime numbers, return an empty array.
"""

def remove_duplicates_and_sort(nums):
    """
    Removes non-prime numbers and duplicates from a list of integers, 
    and returns a sorted list in ascending order.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A sorted list of unique prime numbers.
    """
    def is_prime(n):
        """Checks if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Filter out non-prime numbers and duplicates, and sort the list
    return sorted(set(num for num in nums if is_prime(num)))