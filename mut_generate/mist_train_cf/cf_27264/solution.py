"""
QUESTION:
Create a function `wordFrequencyAnalyzer(text: str)` that takes a string `text` with length between 1 and 10^5 as input. The function should return a list of tuples, where each tuple contains a unique word and its frequency. The output should be sorted by frequency in descending order, and for words with the same frequency, they should be sorted in lexicographical order. The function should consider words in a case-insensitive manner and ignore punctuation. A word is defined as a sequence of non-whitespace characters.
"""

from typing import List, Tuple

def wordFrequencyAnalyzer(text: str) -> List[Tuple[str, int]]:
    # Remove punctuation and convert text to lowercase
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).lower()
    words = text.split()
    
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_word_freq