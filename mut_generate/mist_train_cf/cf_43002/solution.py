"""
QUESTION:
Implement a `vectorize` method that takes a string `doc` as input and returns a NumPy array representing the vectorized form of the document. The vector values for each word are determined by their frequency in the document. The input document contains only lowercase alphabetic characters and spaces. The vector should include all unique words in the document, and the order of words in the vector should follow the order of their appearance in the document.
"""

import numpy as np
from collections import Counter

def vectorize(doc: str) -> np.ndarray:
    """
    Identify the vector values for each word in the given document
    :param doc: a string representing the input document
    :return: a NumPy array representing the vectorized form of the document
    """
    # Split the document into words
    words = doc.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Create a vector with the frequency of each word
    vector = np.array([word_counts[word] for word in words])

    return vector