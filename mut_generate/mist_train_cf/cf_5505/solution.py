"""
QUESTION:
Implement a function `count_unique_words` that takes a string of words separated by spaces as input and returns the count of unique words. The function should be case-insensitive, ignore punctuation marks and special characters, and handle leading and trailing spaces, plural or possessive words, and contractions. Do not use any built-in functions or libraries, and achieve a time complexity of O(n), where n is the length of the input string.
"""

def count_unique_words(string):
    unique_words = set()
    current_word = ''
    string = string.lower()

    for char in string:
        if char.isalnum() or char == "'":
            current_word += char
        elif char == ' ':
            if current_word:
                unique_words.add(current_word)
                current_word = ''

    if current_word:
        unique_words.add(current_word)

    return len(unique_words)