"""
QUESTION:
Write a function `longest_palindrome_substring` that finds the length of the longest substring in the given string that is a palindrome, has an odd length, and contains at least one uppercase letter. The function should use a recursive approach and return 0 if the input string is empty.
"""

def longest_palindrome_substring(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    def helper(s, start, end):
        if start > end:
            return 0
        if start == end:
            if s[start].isupper():
                return 1
            return 0
        if is_palindrome(s[start:end+1]) and (end - start + 1) % 2 != 0:
            return end - start + 1
        return max(helper(s, start + 1, end), helper(s, start, end - 1))

    return helper(s, 0, len(s) - 1)