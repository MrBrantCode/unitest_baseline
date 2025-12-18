"""
QUESTION:
Create a function `append_zeros` that takes two parameters: a string and a maximum number of characters. The function should append zeros to the end of the string until it reaches a length that is a prime number, which is the largest prime number less than or equal to the given maximum number of characters.
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