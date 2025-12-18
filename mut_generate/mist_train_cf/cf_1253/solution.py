"""
QUESTION:
Create a function named `prime_characters` that takes a string as input and returns a tuple containing a list of characters whose Unicode values are prime numbers and the sum of these Unicode values. The function should iterate over each character in the input string, check if its Unicode value is prime, and maintain a list and sum of all prime characters.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_characters(string):
    prime_chars = []
    prime_sum = 0

    for char in string:
        unicode_val = ord(char)
        if is_prime(unicode_val):
            prime_chars.append(char)
            prime_sum += unicode_val

    return prime_chars, prime_sum