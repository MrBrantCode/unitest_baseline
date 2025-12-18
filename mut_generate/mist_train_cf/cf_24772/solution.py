"""
QUESTION:
Create a function called `all_vowels_palindrome` that takes a string `word` as input. This function should return `True` if the input string is a palindrome (i.e., reads the same backward as forward) and contains all the vowels ('a', 'e', 'i', 'o', 'u'), and `False` otherwise. The function is case-sensitive and should consider the input string as is.
"""

def all_vowels_palindrome(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if not word == word[::-1]:
        return False
    for char in vowels:
        if char not in word:
            return False
    return True