"""
QUESTION:
Create a function named `count_upper_prime(s)` that takes an input string `s` and returns the number of uppercase vowel letters situated strictly at prime number indices. Define a helper function `is_prime(n)` to check if a number is prime. The input string `s` is not specified to have any particular length or content restrictions.
"""

def is_prime(n):
    """Helper function to check if a number is prime"""
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

def count_upper_prime(s):
    """
    A function that computes the number of capital vowel letters situated strictly at prime number indices.
    """
    count = 0
    upper_vowels = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(s)):
        # Check if the index is a prime number and the letter at that index is an uppercase vowel
        if is_prime(i) and s[i] in upper_vowels:   
            count += 1
    return count