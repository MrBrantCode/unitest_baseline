"""
QUESTION:
Write a function `longest_palindrome(s)` that finds the longest subsequence composed of consecutive duplicate letter groupings that forms a palindrome in the given string `s`. The function should return the longest palindromic subsequence.
"""

def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            if len(longest) >= j-i:
                break
            elif s[i:j] == s[i:j][::-1]:
                longest = s[i:j]
    return longest