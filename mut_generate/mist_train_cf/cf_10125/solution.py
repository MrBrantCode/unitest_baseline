"""
QUESTION:
Write a function `get_prime_permutations(characters)` that generates all possible permutations of the given set of characters, but only returns the permutations that contain at least one substring of consecutive characters that form a prime number. The input `characters` is a string of digits, and the output should be a list of strings where each string is a permutation of the input characters that meet the condition.
"""

import itertools

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_permutations(characters):
    """
    Generate all possible permutations of a given set of characters,
    keeping only those that contain prime numbers.
    """
    permutations = set()
    for r in range(1, len(characters) + 1):
        # Generate all permutations of length r
        perms = itertools.permutations(characters, r)
        for perm in perms:
            # Convert the permutation to string
            perm_str = ''.join(perm)
            # Check if the permutation contains any prime numbers
            for i in range(len(perm_str)):
                for j in range(i + 1, len(perm_str) + 1):
                    if is_prime(int(perm_str[i:j])):
                        permutations.add(perm_str)
                        break
                if perm_str in permutations:
                    break
    return list(permutations)