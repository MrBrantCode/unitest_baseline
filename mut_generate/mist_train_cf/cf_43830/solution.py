"""
QUESTION:
Write a function called `product_of_primes` that uses a while loop to calculate the product of all prime numbers in a given list of integers. The function should identify prime numbers as those greater than 1 that have no positive divisors other than 1 and themselves.
"""

def product_of_primes(nums):
    """
    Calculate the product of all prime numbers in a given list of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The product of all prime numbers in the list.
    """
    def is_prime(n):
        """Check if a number is prime."""
        if n > 1:
            for i in range(2, int(n/2)+1):
                if (n % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    product = 1
    i = 0
    while i < len(nums):
        if is_prime(nums[i]):
            product *= nums[i]
        i += 1
    return product