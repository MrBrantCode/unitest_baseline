"""
QUESTION:
Extract all instances of a specific word in a given text along with their corresponding indexes, considering case sensitivity. Implement a function named `extract_indexes` that takes two parameters: `text` and `word`. The function should return a list of tuples, where each tuple contains the word and its index in the text.
"""

def extract_indexes(text, word):
    indexes = []
    index = 0

    while index < len(text):
        found = text.find(word, index)

        if found == -1:
            break

        indexes.append((word, found))
        index = found + 1

    return indexes