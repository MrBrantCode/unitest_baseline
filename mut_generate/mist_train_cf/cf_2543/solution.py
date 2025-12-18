"""
QUESTION:
Create a function named `is_valid_string` that takes a string as input and returns `True` if the string meets the following criteria, and `False` otherwise. 

The string must be a palindrome, contain only lowercase letters, and the sum of the ASCII values of the characters in the string must be a prime number.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_valid_string(string):
    return string == string[::-1] and all(97 <= ord(char) <= 122 for char in string) and is_prime(sum(ord(char) for char in string))