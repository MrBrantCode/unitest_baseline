"""
QUESTION:
Write a function `compare_word_sets` that compares two input strings and returns a boolean value indicating whether they contain the same unique words, disregarding uppercase and non-alphanumeric characters, and considering the frequency of each unique word. The function should take two parameters, `phrase1` and `phrase2`, both of type `str`.
"""

def compare_word_sets(phrase1: str, phrase2: str) -> bool:
    import string
    from collections import Counter

    table = str.maketrans('', '', string.punctuation)
    stripped1 = Counter(word.translate(table).lower() for word in phrase1.split())
    stripped2 = Counter(word.translate(table).lower() for word in phrase2.split())

    return stripped1 == stripped2