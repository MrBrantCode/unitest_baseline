"""
QUESTION:
You are given a list of tuples, where each tuple contains a sentence and its corresponding label. Write a function `sort_sentences` that takes this list of tuples as input and returns a new list of tuples sorted by labels in descending order. If two or more sentences have the same label, they should be sorted in lexicographical order.
"""

def entrance(sentences):
    return sorted(sentences, key=lambda item: (-item[1], item[0]))