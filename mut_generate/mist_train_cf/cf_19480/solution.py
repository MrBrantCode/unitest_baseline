"""
QUESTION:
Create a function `hash_string` that assigns a unique number to each input string using a specific prime number algorithm. The function should take a string as input and return the unique hash value. The time complexity should be O(n), where n is the length of the input string, and the space complexity should be O(1). Use a prime number `p` in the hash calculation, and consider using a large prime number `2^32 - 1` to minimize collisions and distribute the hash values evenly.
"""

def hash_string(s):
    """
    Assigns a unique number to each input string using a specific prime number algorithm.

    Args:
    s (str): The input string.

    Returns:
    int: A unique hash value for the input string.

    Time complexity: O(n), where n is the length of the input string.
    Space complexity: O(1), as it only uses a fixed amount of memory.
    """
    p = 2**32 - 1  # A large prime number to minimize collisions
    hash_value = 0

    for c in s:
        hash_value = (hash_value * 31 + ord(c)) % p

    return hash_value