"""
QUESTION:
Write a function named `count_unique_palindromes` that takes a string `input_string` as an input and returns the total number of unique palindromes that can be formed using the characters in the string, considering case sensitivity and ignoring the order of the characters.
"""

import itertools

def is_palindrome(s):
    return s == s[::-1]

def count_unique_palindromes(input_string):
    unique_combinations = set()
    for length in range(1, len(input_string) + 1):
        for comb in itertools.combinations(input_string, length):
            sorted_comb = "".join(sorted(comb))
            if sorted_comb in unique_combinations:
                continue
            unique_combinations.add(sorted_comb)
            if is_palindrome(sorted_comb):
                yield sorted_comb