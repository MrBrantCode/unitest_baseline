"""
QUESTION:
Write a function `largest_palindrome(s)` that takes a string `s` as input and returns the longest palindromic substring from `s`. If there are multiple palindromic substrings of the same maximum length, the function should return the first one it encounters.
"""

def largest_palindrome(s):
    def check(sub):
        return sub == sub[::-1]

    sub_strings = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    palindromes = [sub for sub in sub_strings if check(sub)]
    return max(palindromes, key=len)