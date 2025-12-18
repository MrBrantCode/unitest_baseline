"""
QUESTION:
Construct a function named `count_distinct_lower` that takes a string `s` as input and returns the quantity of diverse lowercase non-vowel characters residing at prime index locations within the string. The index is considered 0-based. The function should only count each character once, regardless of how many times it appears at a prime index.
"""

def count_distinct_lower(s):
    def is_prime(n):
        """helper function to check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    lower_set = set()
    vowels = set('aeiou')
    for i in range(len(s)):
        if is_prime(i) and s[i].islower() and s[i] not in vowels:
            lower_set.add(s[i])
    return len(lower_set)