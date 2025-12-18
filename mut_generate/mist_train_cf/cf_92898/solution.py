"""
QUESTION:
Write a function `count_word_occurrences` that takes a string as input, identifies the words in the string, and returns a dictionary where the keys are the words and the values are their respective counts. The function should ignore case and punctuation. The function should treat numbers as words.
"""

import re
from collections import defaultdict

def count_word_occurrences(input_string):
    """
    This function takes a string as input, identifies the words in the string, 
    and returns a dictionary where the keys are the words and the values are their respective counts.
    
    The function ignores case and punctuation. The function treats numbers as words.
    
    Args:
        input_string (str): The input string.
    
    Returns:
        dict: A dictionary where the keys are the words and the values are their respective counts.
    """
    
    # Remove punctuation and convert to lowercase
    cleaned_string = re.sub(r'[^\w\s]', '', input_string.lower())
    
    # Find all words in the string
    words = re.findall(r'\b\w+\b', cleaned_string)
    
    # Count the occurrences of each word
    word_counts = defaultdict(int)
    for word in words:
        word_counts[word] += 1
    
    return dict(word_counts)