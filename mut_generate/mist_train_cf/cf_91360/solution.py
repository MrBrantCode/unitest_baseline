"""
QUESTION:
Create a function named `word_frequency` that takes a string `text` as input. The function should count the frequency of each word in the text while ignoring case sensitivity and excluding special characters and common English stop words. It should then return or print the top 5 most frequently occurring words along with their frequencies. The word frequencies should be sorted in descending order.
"""

import re
from collections import Counter

def word_frequency(text):
    # Convert text to lowercase and remove special characters
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    
    # Split the cleaned text into words
    words = cleaned_text.split()
    
    # Define common English stop words
    stop_words = ['the', 'is', 'and', 'a']
    
    # Remove stop words from the list of words
    words = [word for word in words if word not in stop_words]
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Sort the word count dictionary by frequency in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top 5 most frequent words
    return sorted_word_count[:5]