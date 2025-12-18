"""
QUESTION:
Create a function named `count_upper_prime(s)` that calculates the count of uppercase vowel characters found strictly at prime number indices in an input string `s`. The function should consider 1-based indexing, so adjust the index accordingly since Python uses 0-based indexing. Define a helper function if necessary to check if a number is prime.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_upper_prime(s):
    upper_vowels = 'AEIOU'
    count = 0
    for i in range(len(s)):
        if is_prime(i+1) and s[i] in upper_vowels:
            count += 1
    return count