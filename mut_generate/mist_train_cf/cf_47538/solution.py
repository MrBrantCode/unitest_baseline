"""
QUESTION:
Create a function named `get_unique_elements` that takes a string parameter. The function should return the count of unique words in the string, considering words as sequences of characters separated by spaces, and ignoring punctuation and different forms of the same word.
"""

def get_unique_elements(sentence):
    # Break the sentence into words and remove punctuation
    words = ''.join(e for e in sentence if e.isalnum() or e.isspace()).lower().split(" ")

    # Use a set to remove duplicates and then return the length of the set
    return len(set(words))