"""
QUESTION:
Create a function `keyword_indices` that takes two parameters: `text` and `keywords`, where `text` is a string and `keywords` is a list of strings. The function should return a dictionary where each key is a keyword from the `keywords` list and the value is a list of indices where the keyword appears in the `text`. If a keyword does not appear in the `text`, the value for that keyword should be -1. The function should be optimized for efficiency when dealing with large strings of text and numerous keywords.
"""

def keyword_indices(text, keywords):
    result = {}
    for keyword in keywords:
        indices = []
        start = text.find(keyword)
        while start != -1:
            indices.append(start)
            start = text.find(keyword, start + 1)
        if indices:
            result[keyword] = indices
        else:
            result[keyword] = -1
    return result