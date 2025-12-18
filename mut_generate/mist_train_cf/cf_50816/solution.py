"""
QUESTION:
Create a function called `longest_palindrome` that takes a string `para` as input. The function should return two values: a boolean indicating whether the entire string is a palindrome when ignoring punctuation, whitespace, and letter casing, and the longest palindromic sub-string within the string. The longest palindromic sub-string should also be determined based on alphanumeric characters only, ignoring punctuation, whitespace, and letter casing.
"""

import re

def longest_palindrome(para):
    para = para.lower()
    para = re.sub(r'\W+', '', para)

    def get_longest_palindrome(s):
        length = len(s)
        palindrome = ""
        for i in range(length):
            for j in range(i + 1, length + 1):
                part = s[i:j]
                if part == part[::-1] and len(part) > len(palindrome):
                    palindrome = part
        return palindrome

    palindrome = para == para[::-1]
    longest_pal = get_longest_palindrome(para)

    return palindrome, longest_pal