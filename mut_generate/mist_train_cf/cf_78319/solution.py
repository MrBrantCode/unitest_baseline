"""
QUESTION:
Create a function `find_smallest_prime` that finds the smallest prime number in a given 2D array. The input array can have up to 1000 rows and 1000 columns. The function should also utilize a helper function `is_prime` to check if a number is prime without using any built-in methods for prime number checks. The time complexity of the solution should not exceed O(n^2).
"""

def is_prime(n):
    """Check if a number is prime."""
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def find_smallest_prime(arr):
    """
    Find the smallest prime number in a given 2D array.

    Args:
        arr (list): A 2D array of integers.

    Returns:
        int or None: The smallest prime number in the array, or None if no prime number is found.
    """
    min_prime = float('inf')
    for row in arr:
        for num in row:
            if is_prime(num) and num < min_prime:
                min_prime = num
    return min_prime if min_prime != float('inf') else None