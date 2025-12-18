"""
QUESTION:
Design a function called `filter_words` that takes a string of text as input and returns a new string containing only the words with 4 or fewer characters.
"""

def filter_words(text):
    filtered_word = []
    words = text.split()

    for word in words:
        if len(word) <= 4:
            filtered_word.append(word)

    return ' '.join(filtered_word)