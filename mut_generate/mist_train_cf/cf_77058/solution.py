"""
QUESTION:
Design a function called `extract_unique_words` that takes a string `s` as input and returns a list of unique words in the string. The function should be case-insensitive, handle punctuation marks by removing them, and consider word frequency and word length. The output list should not include duplicate words.
"""

def extract_unique_words(s):
    s = s.lower()
    words = s.split()
    cleaned_words = []
    for word in words:
        cleaned_word = "".join(char for char in word if char.isalnum())
        cleaned_words.append(cleaned_word)
    return list(set(cleaned_words))