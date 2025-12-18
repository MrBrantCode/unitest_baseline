"""
QUESTION:
Create a function `index_finder(words, targets)` that takes a list of strings `words` and a list of target strings `targets` as input and returns a dictionary where each key is a target string and its corresponding value is a list of indices where the target string or its reverse is found in the `words` list, considering case-sensitivity.
"""

def index_finder(words, targets):
    result = {}
    for target in targets:
        result[target] = [i for i, word in enumerate(words) if word == target or word == target[::-1]]
    return result