"""
QUESTION:
Write a function `get_words(text)` that takes a string `text` as input, splits it into words, removes any punctuation marks or special characters from each word, and returns a list of words that contain more than 10 characters.
"""

def get_words(text):
    return ["".join(e for e in word if e.isalnum()) for word in text.split(" ") if len("".join(e for e in word if e.isalnum())) > 10]