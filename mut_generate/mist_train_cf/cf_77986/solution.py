"""
QUESTION:
Write a function `remove_duplicates(text)` that takes a string of words as input, removes all duplicate words while preserving the original casing, and returns the resulting string with the original order of words maintained. The function should consider 'Word' and 'word' as distinct words.
"""

def remove_duplicates(text):
    words = text.split()
    seen = {}
    result = []
    for word in words:
        if word not in seen:
            seen[word] = True
            result.append(word)
    return " ".join(result)