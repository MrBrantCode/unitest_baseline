"""
QUESTION:
Write a function `count_palindrome_substrings` that takes a string `s` as input and returns the total count of all palindrome substrings in `s`. A single character is also considered a palindrome substring.
"""

def count_palindrome_substrings(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    count = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                count += 1

    return count