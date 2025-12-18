"""
QUESTION:
Design a function `remove_duplicate_words` to take a sentence string as input and return a modified sentence string with all duplicate words removed, preserving the order of the remaining words, and satisfying the following conditions:
- The function should be case-sensitive.
- The order of the remaining words should be the same as the original sentence.
- The function should have a time complexity of O(n), where n is the length of the sentence.
- The function should use only constant extra space.
"""

def remove_duplicate_words(sentence):
    words = sentence.split(" ")
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return " ".join(unique_words)