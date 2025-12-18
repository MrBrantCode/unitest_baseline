"""
QUESTION:
Write a function `longest_substring(string)` that finds the longest substring in the given string which starts with a vowel, ends with a consonant, and contains at least one uppercase letter, without having any repeating characters. The function should return this longest substring.
"""

def longest_substring(string):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    max_len = 0
    longest_sub = ""
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            sub = string[i:j]
            if len(set(sub)) == len(sub) and sub[0] in vowels and sub[-1] in consonants and any(c.isupper() for c in sub) and len(sub) > max_len:
                max_len = len(sub)
                longest_sub = sub
    return longest_sub