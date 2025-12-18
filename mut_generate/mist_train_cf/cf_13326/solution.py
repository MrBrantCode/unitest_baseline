"""
QUESTION:
Write a function named `longest_word` that takes a string of alphabetical characters and spaces as input and returns the first occurrence of the longest word. If multiple words have the same maximum length, return the first occurrence of such a word.
"""

def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest