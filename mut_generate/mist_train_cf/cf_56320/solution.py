"""
QUESTION:
Create a function `process_paragraph(paragraph)` that takes a string paragraph as input and returns a dictionary of palindrome words and their counts, along with a dictionary of their ranks. The function should handle any type of punctuation, multiple sentence structures, and be case-insensitive. The function should also exclude single-letter words from being considered as palindromes.
"""

import re
from collections import Counter

def process_paragraph(paragraph):
    """
    Takes a string paragraph as input and returns a dictionary of palindrome words and their counts, 
    along with a dictionary of their ranks.

    Args:
        paragraph (str): The input paragraph.

    Returns:
        tuple: A tuple containing two dictionaries. The first dictionary contains palindrome words as keys 
        and their counts as values. The second dictionary contains palindrome words as keys and their 
        ranks as values.
    """
    # Make everything lowercase
    paragraph = paragraph.lower()
    # Strip symbols
    paragraph = re.sub('[^a-zA-Z ]', '', paragraph)
    # Split by spaces
    words = paragraph.split()
    # Filter down to just palindromes (excluding single-letter words) and count
    palindromes = Counter([word for word in words if len(word) > 1 and word == word[::-1]])
    # Rank
    rankings = {word: rank+1 for rank, (word, count) in enumerate(palindromes.most_common())}
    return palindromes, rankings