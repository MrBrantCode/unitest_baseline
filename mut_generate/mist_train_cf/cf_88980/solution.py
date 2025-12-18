"""
QUESTION:
Implement the function `count_unique_words(string)` to count the number of unique words in a given string. The words are case-insensitive, and punctuation marks or special characters should be ignored. The function should handle leading and trailing spaces, plural or possessive words, and contractions. The solution should have a time complexity of O(n), where n is the length of the input string, and must be implemented manually without using any built-in functions or libraries.
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