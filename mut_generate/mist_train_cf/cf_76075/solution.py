"""
QUESTION:
Write a function `primes_at_prime_indices` that takes a list of non-negative integers as input and returns a new list containing prime numbers at their respective prime indices. If the input list contains non-integer or negative values, the function should return an error message. The function should also be optimized for large lists, and if a non-prime number is found at a prime index, it should be replaced with 0 in the output list.
"""

def primes_at_prime_indices(num_list):
    if not all([isinstance(num, int) and num >= 0 for num in num_list]):
        return "Error: List should contain only non-negative integers."

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_indices = [idx for idx in range(2, len(num_list)) if is_prime(idx)]
    return [num_list[idx] if is_prime(num_list[idx]) else 0 for idx in prime_indices]