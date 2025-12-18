"""
QUESTION:
Write a function named `is_five_letter_palindrome` that checks if a given string consists of exactly 5 alphabetic characters and is a palindrome, regardless of the case of the letters. The function should return a boolean value.
"""

def is_five_letter_palindrome(word):
    if len(word) != 5:
        return False
    word = word.lower()
    for char in word:
        if not char.isalpha():
            return False
    if word != word[::-1]:
        return False
    return True