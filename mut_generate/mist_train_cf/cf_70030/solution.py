"""
QUESTION:
Write a function named `count_prime_vowels(s)` that takes a string `s` as input and returns the number of lowercase vowels in the string that are located at prime indices. A prime index is an index in the string (0-based) that is a prime number. A lowercase vowel is one of the characters 'a', 'e', 'i', 'o', or 'u'. The function should return the count of such characters.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def count_prime_vowels(s):
    count = 0
    vowels = set('aeiou')
    for i, char in enumerate(s):
        if is_prime(i) and char.lower() in vowels:
            count += 1
    return count