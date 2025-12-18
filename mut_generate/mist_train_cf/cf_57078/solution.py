"""
QUESTION:
Create a function named `filter_prime_by_char` that takes a dictionary `d` and a character `char` as input. The function should return a new dictionary containing only the entries from `d` where the key starts with the given character and the corresponding value is a prime number.
"""

def filter_prime_by_char(d, char):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    return {k: v for k, v in d.items() if k.startswith(char) and is_prime(v)}