"""
QUESTION:
Write a function `count_hello_permutations(s)` that takes a string `s` as input and returns a tuple of a boolean and an integer. The boolean should be `True` if the string contains any permutation of the word "Hello" (ignoring case sensitivity), and `False` otherwise. The integer should represent the number of permutations found. The function should not exceed O(n log n) time complexity.
"""

from collections import Counter

def count_hello_permutations(s):
    s = s.lower()
    counter = 0
    hello_counter = Counter('hello')

    for i in range(len(s)-4):
        if hello_counter == Counter(s[i:i+5]):
            counter += 1
    return counter > 0, counter