"""
QUESTION:
Create a function named `count_occurrences` that takes a string sentence as input and returns a dictionary where the keys are the unique words in the sentence and the values are their respective occurrence counts. The function should be case-insensitive, ignore special characters and punctuation, and handle multiple spaces between words. It should also treat emojis as words.
"""

import re

def count_occurrences(sentence):
    # Remove special characters and emojis using regular expression
    cleaned_sentence = re.sub(r'[^\w\s\d\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]+', '', sentence)
    
    # Convert the sentence to lowercase
    cleaned_sentence = cleaned_sentence.lower()
    
    # Split the sentence into individual words
    words = cleaned_sentence.split()
    
    # Create a dictionary to store the word counts
    word_counts = {}
    
    # Iterate through each word and count its occurrences
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts