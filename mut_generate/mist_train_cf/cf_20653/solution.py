"""
QUESTION:
Write a function `longest_palindrome_odd_length` to find the length of the longest substring in a given string that is a palindrome, has an odd length, and contains at least one uppercase letter. The substring should not contain any repeated characters.
"""

def longest_palindrome_odd_length(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    def has_uppercase(sub):
        return any(char.isupper() for char in sub)

    def has_no_repeats(sub):
        return len(sub) == len(set(sub))

    max_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            if len(sub) % 2 != 1:
                continue
            if is_palindrome(sub) and has_uppercase(sub) and has_no_repeats(sub):
                max_length = max(max_length, len(sub))
    return max_length