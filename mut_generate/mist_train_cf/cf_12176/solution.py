"""
QUESTION:
Create a function called `get_primes_up_to_n` that takes an integer `n` as input and returns a list of all prime numbers from 1 to `n` (inclusive). The function should be efficient and able to handle large values of `n`. The output should be a list of integers in ascending order.
"""

def get_primes_up_to_n(n):
    """
    Returns a list of all prime numbers from 1 to n (inclusive).

    Args:
        n (int): The upper limit for generating prime numbers.

    Returns:
        list: A list of prime numbers from 1 to n in ascending order.
    """
    prime_numbers = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)
    return prime_numbers