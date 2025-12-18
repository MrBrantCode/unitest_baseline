"""
QUESTION:
Write a function `convert` that takes a string of words as input. It should return a new string where the first letter of every alternate word in the original string is converted to uppercase.
"""

def convert(text):
    words = text.split(" ")
    for i in range(len(words)):
        # check if word is alternate
        if i % 2 != 0:
            # convert first letter to uppercase
            words[i] = words[i].capitalize()
    return " ".join(words)