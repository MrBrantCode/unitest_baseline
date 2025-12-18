"""
QUESTION:
Write a function `prime_length_substrings(sentence)` that takes a string of alphabetical characters with spaces as input. Return a new string containing substrings from the initial sentence, where the substring lengths are exclusively prime numbers, maintaining the original sequence of substrings, and no two substrings should share the same characters. If multiple solutions exist, return the substring with the highest frequency of vowels. The input string has a length between 1 and 100, contains solely alphabetical characters, and each vowel is capitalized. Substrings can only be formed by removing spaces.
"""

import re
from collections import Counter

def prime_length_substrings(sentence):
    vowel_count = lambda word: sum(1 for ch in word if ch in 'AEIOUaeiou')
    is_prime = lambda no: all([(no%j) for j in range(2, int(no**0.5)+1)]) and no > 1

    words = re.findall(r'\b\w+\b', sentence)
    prime_words = [w for w in words if is_prime(len(w))]

    if not prime_words:
        return ""

    max_vowel_count = max(vowel_count(w) for w in prime_words)
    return max([w for w in prime_words if vowel_count(w) == max_vowel_count], key=len)