"""
QUESTION:
Develop a function named `calculate_frequency` that takes a string `paragraph` as input and returns the frequency of each unique word, the frequency of each unique character (excluding white space), the most frequently occurring word, and the most frequently occurring character. The function should ignore case sensitivity (i.e., handle upper-case and lower-case as the same).
"""

from collections import Counter
import re

def calculate_frequency(paragraph):
    # Convert text to lower case and replace non-word characters with space
    processed_para = re.sub(r'\W', ' ', paragraph.lower())
    
    # Split the text into words
    words = processed_para.split()
    
    # Calculate word frequency
    word_freq = Counter(words)
    
    # Calculate character frequency (excluding white space)
    char_freq = Counter(processed_para.replace(' ', ''))
    
    # Find the most common word and character
    common_word = word_freq.most_common(1)
    common_char = char_freq.most_common(1)
    
    return word_freq, char_freq, common_word, common_char