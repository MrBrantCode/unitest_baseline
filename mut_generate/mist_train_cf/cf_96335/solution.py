"""
QUESTION:
Write a function `compare_primes(A, B)` that takes two integers as input. It should first check if both numbers are prime and within the range of 1 to 1000. If both conditions are met, it should return "A is greater than B" if A is greater than B, otherwise, it should return nothing or a message indicating the condition is not met.
"""

def compare_primes(A, B):
    """
    Compare two prime numbers within the range of 1 to 1000.

    Args:
    A (int): The first prime number.
    B (int): The second prime number.

    Returns:
    str or None: "A is greater than B" if both numbers are prime and A is greater than B, otherwise None.
    """
    def is_prime(num):
        if num < 2 or num > 1000:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if is_prime(A) and is_prime(B):
        if A > B:
            return "A is greater than B"
    return None