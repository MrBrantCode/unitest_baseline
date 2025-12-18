"""
QUESTION:
Implement a function `wordFrequency(text: str, stopWords: List[str]) -> Dict[str, int]` that takes a string `text` and a list of strings `stopWords` as input. The function should return a dictionary where the keys are the unique words in the text (ignoring case and punctuation) and the values are the frequencies of those words, excluding the stop words. The function should consider words regardless of their case and should ignore punctuation.
"""

from typing import List, Dict
import re
from collections import Counter

def word_frequency(text: str, stopWords: List[str]) -> Dict[str, int]:
    # Convert text to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split the text into words
    words = text.split()
    
    # Remove stop words
    words = [word for word in words if word not in stopWords]
    
    # Count the frequency of each word
    frequency = Counter(words)
    
    return dict(frequency)