"""
QUESTION:
Develop a function `is_subsequence` that takes two number strings `s1` and `s2` as input and returns a boolean value. The function should check if all digits of `s2` appear in the same order in `s1`, and each digit of `s2` is a prime number (2, 3, 5, or 7). The function should return `True` if the subsequence is valid and `False` otherwise.
"""

def is_subsequence(s1, s2):
    primeNumbers = set(str(i) for i in [2, 3, 5, 7])
    j = 0
    for i in range(len(s1)):
        if j < len(s2) and s2[j] == s1[i]:
            if s2[j] not in primeNumbers:
                return False
            j += 1
    return (j == len(s2))