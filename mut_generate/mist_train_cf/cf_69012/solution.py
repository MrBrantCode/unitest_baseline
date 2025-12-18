"""
QUESTION:
Create a function `check_prime_hash(n, hash_function)` that takes an integer `n` and a hash function `hash_function` as input, and returns `True` if `n` is a prime number and `False` otherwise. The function should utilize a hash table to store the primality of previously checked numbers. Implement a custom hash function `generate_hash(n)` to compute the hash value of `n`. The function should handle integers of any size and return accurate results. Note that the `hash_function` should take an integer `n` as input and return a unique hash value.
"""

# Global variable used for hash table of prime numbers
hash_table = {}

# Auxilary function to generate hash value
def generate_hash(n):
    """
    A hash function that generates an unique hash value. This value is key in the hash table.
    Hash is calculated by taking a modulo of multiplication of given integer with large prime and small prime.
    """
    large_prime, small_prime = 8182317823182317, 239
    return ((n * large_prime * small_prime) % 1000000007)

# Function to check prime number by using a hash table
def check_prime_hash(n, hash_function):
    """
    Returns true for prime integers, false for non-prime integers. Utilises a hash table and an
    unconventional optimization technique. Requires a hash function to compute the hash of 'n'.
    """
    if n in hash_table:
        return hash_table[n]
    if n < 2:
        hash_table[n] = False
        return False
    if n == 2:
        hash_table[n] = True
        return True
    if n % 2 == 0:
        hash_table[n] = False
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            hash_table[n] = False
            return False
        i += 2

    hash_key = hash_function(n)
    hash_table[hash_key] = True
    return True