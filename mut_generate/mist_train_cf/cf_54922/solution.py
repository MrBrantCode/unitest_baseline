"""
QUESTION:
Write a function named `count_capital_vowels` that takes a list of strings as input and returns the total count of uppercase vowel letters ('A', 'E', 'I', 'O', 'U') in the list.
"""

def count_capital_vowels(arr):
    return sum(word.count(letter) for word in arr for letter in "AEIOU")