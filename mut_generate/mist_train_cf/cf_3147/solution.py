"""
QUESTION:
Write a function named `most_common_words` that takes two parameters: a string `text` and a positive integer `k`. The function should return a list of the top `k` most common words in the `text`, excluding common stop words and ignoring punctuation and case. In case of a tie in frequency, words should be sorted alphabetically. The time complexity of the function should be O(nlogn), where n is the length of the input `text`.
"""

import re
from collections import Counter

def most_common_words(text, k):
    # Remove punctuation and convert to lowercase
    text = re.sub('['+re.escape(string.punctuation)+']', '', text.lower())
    
    # Split text into words
    words = text.split()
    
    # Define stop words
    stop_words = set(['the', 'and', 'in', 'to', 'it', 'is', 'a'])
    
    # Count the frequency of each word
    word_counts = Counter(word for word in words if word not in stop_words)
    
    # Sort the words by frequency (in descending order) and alphabetically
    sorted_words = sorted(word_counts.keys(), key=lambda x: (-word_counts[x], x))
    
    # Return the top k most common words
    return sorted_words[:k]