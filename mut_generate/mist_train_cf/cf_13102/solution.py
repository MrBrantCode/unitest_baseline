"""
QUESTION:
Create a function `append_zeros` that takes a string and a maximum number of characters as input, determines the nearest prime number less than or equal to the given maximum number of characters, and appends zeros to the string up to that length. The function should return the resulting string. The maximum number of characters must be a prime number.
"""

def append_zeros(string, max_chars):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_max_chars = max_chars
    while not is_prime(prime_max_chars):
        prime_max_chars -= 1

    return string + "0" * (prime_max_chars - len(string))