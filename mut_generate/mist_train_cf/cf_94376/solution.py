"""
QUESTION:
Write a function `remove_vowels(sentence)` that takes a string `sentence` as input and returns the string with all vowels removed. The input string may contain punctuation marks, special characters, and multiple spaces between words. The function should preserve the original order and spacing of non-vowel characters in the input string.
"""

def remove_vowels(sentence):
    vowels = "aeiouAEIOU"
    modified_sentence = ""
    for char in sentence:
        if char not in vowels:
            modified_sentence += char
    return modified_sentence