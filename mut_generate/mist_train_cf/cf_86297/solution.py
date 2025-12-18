"""
QUESTION:
Write a function named `count_unique_words` that takes a string `text` as input and returns the number of unique words in the text, ignoring case, leading/trailing spaces, punctuation marks, and special characters. The time complexity of the solution should be O(n) and the space complexity should be O(n), where n is the number of characters in the text.
"""

def count_unique_words(text):
    text = text.lower().strip()
    words = text.split()
    unique_words = set()

    for word in words:
        word = ''.join(e for e in word if e.isalnum())
        unique_words.add(word)

    return len(unique_words)