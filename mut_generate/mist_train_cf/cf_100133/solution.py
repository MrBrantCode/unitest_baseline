"""
QUESTION:
Write a function `longest_palindrome` that takes a list of words as input and returns the longest palindrome present in the list. A palindrome is a word that reads the same backward as forward. If no palindromes exist in the list, return an empty string.
"""

def longest_palindrome(words):
    longest = ""
    for word in words:
        if word == word[::-1] and len(word) > len(longest):
            longest = word
    return longest