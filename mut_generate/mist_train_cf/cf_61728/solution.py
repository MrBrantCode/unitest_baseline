"""
QUESTION:
Write a function `find_palindrome(words, target)` that takes a list of words and a target word as input, and returns `True` if the target word is a palindrome and exists in the list, and `False` otherwise.
"""

def find_palindrome(words, target):
    for word in words:
        if word == target and word == word[::-1]: # check if the word is equal to target and its reverse
            return True
    return False