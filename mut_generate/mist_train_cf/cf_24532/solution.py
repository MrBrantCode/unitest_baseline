"""
QUESTION:
Create a function named `is_prime_array` to generate an array of all prime numbers up to a given number `n`, in this case, 50. The function should return an array of integers. The input number `n` is a positive integer.
"""

def is_prime_array(n):
    """
    Generate an array of all prime numbers up to a given number n.

    Args:
    n (int): A positive integer.

    Returns:
    list: A list of prime numbers up to n.
    """
    def is_prime(num):
        """Check if a number is prime."""
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    return [i for i in range(2, n + 1) if is_prime(i)]