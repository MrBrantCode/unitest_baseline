"""
QUESTION:
Write a function named `extract_unique_words` that takes a string as input, splits it into words, and returns a list of unique words in their order of occurrence. The function should preserve the original order of words and exclude any duplicates. The input string may contain punctuation attached to words, and such punctuation should be treated as part of the word.
"""

def extract_unique_words(string):
    words = string.split()
    unique_words = set()
    unique_words_ordered = []

    for word in words:
        if word not in unique_words:
            unique_words.add(word)
            unique_words_ordered.append(word)

    return unique_words_ordered