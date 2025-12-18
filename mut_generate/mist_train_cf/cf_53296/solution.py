"""
QUESTION:
Write a function `prime_ascii_sum` that takes a string as input, calculates the sum of ASCII values of all characters in the string, and returns True if the sum is a prime number, False otherwise.
"""

def prime_ascii_sum(s):
    def is_prime(n):
        if n <= 1: 
            return False
        if n == 2 or n == 3: 
            return True
        if n % 2 == 0 or n % 3 == 0: 
            return False
        for i in range(5, int(n**0.5) + 1, 6): 
            if n % i == 0 or n % (i + 2) == 0: 
                return False
        return True

    ascii_sum = sum(ord(char) for char in s)
    return is_prime(ascii_sum)