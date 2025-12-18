"""
QUESTION:
Create a function named `get_most_frequent_words` that takes four parameters: a string `string`, a list of stop words `stop_words`, the minimum word length `min_word_length`, and the number of words to return `num_words`. The function should return the `num_words` most frequent words in the string, excluding the stop words and words with a length less than `min_word_length`. The function should handle cases and punctuation marks properly.
"""

import re
from collections import Counter

def get_most_frequent_words(string, stop_words, min_word_length, num_words):
    # Convert the string to lowercase
    string = string.lower()
    
    # Remove punctuation marks using regular expression
    string = re.sub(r'[^\w\s]', '', string)
    
    # Split the string into words
    words = string.split()
    
    # Exclude stop words and words less than min_word_length
    words = [word for word in words if word not in stop_words and len(word) >= min_word_length]
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Get the most frequent words
    most_frequent_words = word_counts.most_common(num_words)
    
    return most_frequent_words