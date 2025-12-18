"""
QUESTION:
Create a function called `word_frequency` that takes a string as input. The function should remove punctuation marks, special characters, and numbers from the string, and then count the occurrences of each unique word in a case-insensitive manner. The function should return a list of tuples, where each tuple contains a unique word and its corresponding frequency, sorted in descending order based on the frequency.
"""

import re
from collections import Counter

def word_frequency(text):
    # Remove punctuation marks, special characters, and numbers
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert the text to lowercase
    cleaned_text = cleaned_text.lower()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Count the occurrences of each word
    word_counts = Counter(words)
    
    # Sort the words in descending order based on their frequency
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_words