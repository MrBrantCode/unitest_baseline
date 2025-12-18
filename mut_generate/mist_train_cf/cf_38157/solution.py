"""
QUESTION:
Create a function called `word_frequency` that calculates the frequency of each word in a given text. The function should ignore case, remove punctuation, and consider "Word" and "word" as the same word. It should output the unique words in alphabetical order along with their frequencies. The input is a string and the output is a list of word frequencies in alphabetical order.
"""

import re
from typing import List, Tuple

def word_frequency(text: str) -> List[Tuple[str, int]]:
    """
    This function calculates the frequency of each word in a given text.
    
    It ignores case, removes punctuation, and considers "Word" and "word" as the same word.
    
    Args:
        text (str): The input text.
    
    Returns:
        List[Tuple[str, int]]: A list of tuples containing unique words and their frequencies in alphabetical order.
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', '', text).lower()
    words = text.split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort the words alphabetically
    sorted_words = sorted(word_count.items())
    
    return sorted_words