"""
QUESTION:
Write a function named `count_characters` that takes a phrase as input and returns the total count of alphabetic characters in the phrase, ignoring spaces and punctuation. The function should only count letters from the English alphabet (a-z or A-Z).
"""

def count_characters(phrase):
    count = 0
    for char in phrase:
        if char.isalpha():
            count += 1
    return count