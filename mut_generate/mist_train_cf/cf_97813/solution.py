"""
QUESTION:
Write a function `longest_palindrome` that takes a list of words as input and returns the longest palindrome present in the list. The function should check each word in the list to see if it reads the same backward as forward, and return the longest word that meets this condition. If there are multiple palindromes of the same length, any one can be returned.
"""

def longest_palindrome(words):
    longest = ""
    for word in words:
        if word == word[::-1] and len(word) > len(longest):
            longest = word
    return longest