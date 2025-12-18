"""
QUESTION:
Create a function `count_frequent_words` that takes a paragraph and a list of stop words as input, and returns the top 10 most frequent words and their counts in the paragraph, excluding the stop words and ignoring case. The function should also exclude punctuation. 

The function should use regular expressions to filter out the punctuation and split the paragraph into words. It should use a case-insensitive comparison for the stop words.
"""

import re
from collections import Counter

def count_frequent_words(paragraph, stop_words):
    """
    Returns the top 10 most frequent words and their counts in the paragraph, 
    excluding the stop words and ignoring case.

    Parameters:
    paragraph (str): The input paragraph.
    stop_words (list): A list of stop words to be excluded.

    Returns:
    dict: A dictionary with the top 10 most frequent words and their counts.
    """
    # filter stopwords and punctuation, then count distinct words
    words = re.sub(r'[^\w\s]', '', paragraph.lower()).split()
    words = [word for word in words if word not in stop_words]
    word_counts = Counter(words)

    # return top 10
    return dict(word_counts.most_common(10))