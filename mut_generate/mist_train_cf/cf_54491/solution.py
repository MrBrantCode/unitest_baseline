"""
QUESTION:
Design a function called `detect_plagiarism` that takes two strings `doc1` and `doc2` as input and returns a boolean indicating whether `doc2` is plagiarized from `doc1`. The function should use a simplified algorithm that checks for the frequency of words in both documents and returns `True` if more than a certain percentage (say, 90%) of the words from `doc2` appear in `doc1` with similar frequencies. The function should also perform text normalization by removing punctuation, special characters, and converting text to lower-case.
"""

import re
from collections import Counter

def detect_plagiarism(doc1, doc2):
    """
    Detects plagiarism in doc2 from doc1 based on word frequency similarity.

    Args:
    doc1 (str): The original document.
    doc2 (str): The document to check for plagiarism.

    Returns:
    bool: True if doc2 is plagiarized from doc1, False otherwise.
    """

    # Define the plagiarism threshold (90%)
    threshold = 0.9

    # Perform text normalization (remove punctuation, special characters, and convert to lower-case)
    doc1 = re.sub(r'[^\w\s]', '', doc1).lower()
    doc2 = re.sub(r'[^\w\s]', '', doc2).lower()

    # Split the documents into individual words
    words1 = doc1.split()
    words2 = doc2.split()

    # Count the frequency of each word in both documents
    freq1 = Counter(words1)
    freq2 = Counter(words2)

    # Calculate the number of common words
    common_words = sum(min(freq1[word], freq2[word]) for word in freq1 if word in freq2)

    # Calculate the plagiarism percentage
    plagiarism_percentage = common_words / len(words2)

    # Return True if the plagiarism percentage exceeds the threshold
    return plagiarism_percentage > threshold