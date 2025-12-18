"""
QUESTION:
Create a function `word_count_analysis` that takes a string `text` as input and returns a list of tuples, where each tuple contains a unique word and its count, sorted in descending order of frequency. The function should ignore the case of the letters, consider words with the same characters but different cases as the same word, and exclude common English stop words. The input string may contain non-alphanumeric characters, which should be treated as word separators.
"""

from typing import List, Tuple
import re
from collections import Counter

def word_count_analysis(text: str) -> List[Tuple[str, int]]:
    # Convert the text to lowercase and split it into words using regex
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Define common English stop words
    stop_words = {'the', 'and', 'or', 'but', 'for', 'as', 'in', 'are', 'is', 'can', 'these', 'a', 'an', 'to', 'of', 'on', 'at', 'with', 'by', 'from', 'it', 'its', 'that', 'this', 'there', 'which', 'who', 'what', 'where', 'when', 'how', 'why', 'not', 'no', 'yes', 'true', 'false'}
    
    # Filter out stop words and count the occurrences of each word
    word_counts = Counter(word for word in words if word not in stop_words)
    
    # Sort the word counts in descending order of frequency
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_counts