"""
QUESTION:
Create a function named `count_words(sentence)` that takes a string as an input and returns the number of words in the sentence. The function should handle punctuation marks or special characters by treating them as word delimiters.
"""

def count_words(sentence):
    # Remove any punctuation marks or special characters
    cleaned_sentence = ''.join(c if c.isalnum() else ' ' for c in sentence)
    
    # Split the cleaned sentence into a list of words
    words = cleaned_sentence.split()
    
    # Return the number of words
    return len(words)