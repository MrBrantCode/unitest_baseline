"""
QUESTION:
Write a function `check_palindrome(word)` that determines whether a given word is a palindrome. A palindrome is a word that reads the same backwards as forwards, ignoring case. The function should return a string indicating whether the word is a palindrome or not.
"""

def check_palindrome(word):
    word = word.lower()  # make it case-insensitive
    reversed_word = word[::-1]  # reverse the word
    
    if word == reversed_word:
        return "Characteristics of a palindrome present."
    else:
        return "Characteristics of a palindrome absent."