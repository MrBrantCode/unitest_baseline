"""
QUESTION:
Write a function `find_palindrome` that takes a list of words and a target word as input. The function should find and return the target word from the list if it is a palindrome, otherwise return a message indicating no palindromic target was found.
"""

def find_palindrome(words, target):
    for word in words:
        if word == word[::-1] and word == target:
            return word

    return "No palindromic target found"