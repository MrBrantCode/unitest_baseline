"""
QUESTION:
Create a function `punctuation_to_hyphen(text)` that takes a string `text` as input and returns the string with all punctuation marks replaced with hyphens. The function should consider punctuation marks like semi-colons, colons, question marks, brackets, single & double quotes, etc.
"""

def punctuation_to_hyphen(text):
    punctuation = "!@#$%^&*()_+{}|:\"<>?,./;'[]\\-="
    for i in range(len(punctuation)):
        if punctuation[i] in text:
            text = text.replace(punctuation[i], "-")
    return text