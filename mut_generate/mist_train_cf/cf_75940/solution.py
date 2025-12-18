"""
QUESTION:
Write a function `check_words(s)` that accepts a string `s` as input and returns a boolean value indicating whether every word in the string begins and ends with the same letter, ignoring case sensitivity and punctuation.
"""

def check_words(s):
    import string
    s = s.translate(str.maketrans('', '', string.punctuation))
    words = s.split()
    for word in words:
        if word[0].lower() != word[-1].lower():
            return False
    return True