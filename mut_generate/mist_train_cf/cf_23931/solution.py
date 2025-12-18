"""
QUESTION:
Write a function `find_words_with_al` that takes a list of words as input and returns a list of words that contain the substring "al". The input list contains a mix of words, and the function should be case-sensitive.
"""

def find_words_with_al(words):
    return [word for word in words if "al" in word]