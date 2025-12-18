"""
QUESTION:
Write a function `duplicate_words(text, num)` that takes a string `text` and an integer `num` as input and returns a string where each word in `text` is duplicated `num` times. The words in the output string should be separated by a space.
"""

def duplicate_words(text, num):
    words = text.split(" ")
    words = [word * num for word in words]
    return " ".join(words)