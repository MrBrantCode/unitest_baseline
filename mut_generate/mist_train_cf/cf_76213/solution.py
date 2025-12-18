"""
QUESTION:
Write a function `starts_with_t(words)` that takes a list of strings `words` as input. The function should return the first string in the list that starts with "t" (case-insensitive) after ignoring any leading whitespace. If no such string exists, the function should return `None`.
"""

def starts_with_t(words):
    for word in words:
        stripped_word = word.lstrip()
        if stripped_word and stripped_word[0].lower() == "t":
            return stripped_word
    return None