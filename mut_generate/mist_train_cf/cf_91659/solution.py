"""
QUESTION:
Write a function `extract_unique_words(string)` that takes a string as input, splits it into words, and returns a list of unique words while preserving their original order of occurrence. The function should ignore duplicates and maintain the order in which each word first appears in the string.
"""

def extract_unique_words(string):
    # Split the string into words
    words = string.split()

    # Create an empty set to store unique words
    unique_words = set()

    # Create a list to preserve the order of occurrence
    unique_words_ordered = []

    # Iterate through each word in the original order
    for word in words:
        # If the word is not already in the set, add it to the set and list
        if word not in unique_words:
            unique_words.add(word)
            unique_words_ordered.append(word)

    return unique_words_ordered