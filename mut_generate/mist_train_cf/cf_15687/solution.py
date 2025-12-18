"""
QUESTION:
Write a function named `count_occurrences` that takes two parameters: a text string and a target word string. The function should return the number of occurrences of the target word in the text, ignoring case sensitivity and counting only standalone occurrences of the word.
"""

def count_occurrences(text, word):
    text = text.lower()
    words = text.split()
    count = 0
    for w in words:
        if w == word.lower():
            count += 1
    return count