"""
QUESTION:
Create a function `analyze_text` that takes a string `text` as input. The function should return a dictionary with the frequency of each word in the text, excluding common stop words and special characters, and a list of the top 3 most frequently occurring words. The function should handle large text inputs efficiently and be case-insensitive. The stop words that should be excluded are not limited to 'the', 'is', 'a', and other common English stop words.
"""

import re
from collections import Counter

def analyze_text(text):
    # Define stop words
    stop_words = set(['the', 'is', 'a', 'and', 'it', 'with', 'while'])
    
    # Remove special characters and punctuation marks
    clean_text = re.sub(r'[^\w\s]', '', text)
    
    # Convert text to lowercase and split into words
    words = clean_text.lower().split()
    
    # Remove stop words
    words = [word for word in words if word not in stop_words]
    
    # Count word frequency
    word_count = Counter(words)
    
    # Get top 3 most frequently occurring words
    top_words = word_count.most_common(3)
    
    return word_count, top_words