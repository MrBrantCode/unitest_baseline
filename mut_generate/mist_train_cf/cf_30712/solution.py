"""
QUESTION:
Implement a function `pattern_matcher(patterns, texts)` that returns a list of lists where each inner list contains the indices of the texts that match the corresponding pattern. The function takes two lists as input: `patterns` and `texts`, where `patterns` is a list of strings representing patterns and `texts` is a list of strings representing texts. The function should return an empty inner list if a pattern does not match any text. Assume that the input lists are non-empty and the lengths of the pattern and text lists are not necessarily the same.
"""

def pattern_matcher(patterns, texts):
    result = []
    for pattern in patterns:
        matches = [i for i, text in enumerate(texts) if pattern in text]
        result.append(matches)
    return result