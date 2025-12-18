"""
QUESTION:
Write a function `most_frequent_word(text: str) -> str` that takes a string of text as input and returns the most frequent word in the text, considering the word frequency case-insensitively. The function should ignore word order and return the word with the highest frequency.
"""

def most_frequent_word(text: str) -> str:
    words = text.lower().split()
    word_count = {}
    max_count = 0
    max_word = ''
    for word in words:
        word = ''.join(e for e in word if e.isalnum())  # remove punctuation
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
        if word_count[word] > max_count:
            max_count = word_count[word]
            max_word = word
    return max_word