"""
QUESTION:
Create a function named `count_prime_vowels(s)` that takes a string `s` as input. The function should return the count of lowercase vowels situated in prime-numbered indices within the input string. The indices are 0-based. A prime index is an index that is a prime number.
"""

def count_prime_vowels(s):
    count = 0
    vowels = set('aeiou')
    for i in range(len(s)):
        if is_prime(i) and s[i].lower() in vowels:
            count += 1
    return count

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_div = int(n**0.5) + 1
    for i in range(3, max_div, 2):
        if n % i == 0:
            return False
    return True