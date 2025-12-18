"""
QUESTION:
Create a function called `convert_sentence(sentence)` that takes a sentence as input and returns a list of words. The list should exclude words that start with a vowel (a, e, i, o, u) and have more than 3 letters. The remaining words should be in alphabetical order. The function should be case-insensitive when checking for vowels.
"""

def convert_sentence(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = sentence.split()
    result = [word for word in words if word[0].lower() not in vowels and len(word) <= 3]
    result.sort()
    return result