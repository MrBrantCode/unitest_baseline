"""
QUESTION:
Create a function `prime_index_and_value` that takes a list of integers as input and returns a new list containing prime numbers from the input list that are situated at their corresponding prime indices (1-based index). The function should handle exceptions for non-integer and negative inputs. The function should be able to handle extensive lists.
"""

def prime_index_and_value(num_list):
    if len(num_list) < 2:
        return []

    def is_prime(n):
        if not isinstance(n, int) or n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes_to_n(n):
        primes = []
        for possiblePrime in range(2, n + 1):
            if is_prime(possiblePrime):
                primes.append(possiblePrime)
        return primes

    prime_indices = get_primes_to_n(len(num_list))
    prime_list = [num_list[i-1] for i in prime_indices if is_prime(num_list[i-1])]

    return prime_list