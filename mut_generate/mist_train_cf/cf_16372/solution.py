"""
QUESTION:
Write a function called `count_letters` that takes a string as input and returns a dictionary where the keys are the letters in the string and the values are their respective counts, ignoring case and non-alphabet characters.
"""

def count_letters(string):
    letter_count = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count