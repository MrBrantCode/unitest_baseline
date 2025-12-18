"""
QUESTION:
Create a function named `analyze_text` that takes a string `text` as input and returns a dictionary of word frequencies and a list of the top 3 most frequently occurring words. The function should exclude common stop words and ignore special characters and punctuation marks. It should be efficient enough to handle large text inputs within a reasonable time limit.
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