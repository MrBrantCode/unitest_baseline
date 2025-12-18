"""
QUESTION:
Implement a function called `generate_summary` that takes two parameters: a string of text and the maximum number of words in the summary. The function should return a string summary of the text, limited to the specified number of words. The summary should capture the main ideas and key details of the original text.

Assume the input text is in English and does not contain special characters or symbols. The function should handle large input texts efficiently and include error handling for the following scenarios: empty or whitespace-only input text, invalid maximum number of words, and the case where no sentences meet the selection criteria.
"""

import re
import heapq
from collections import defaultdict

def generate_summary(text, max_words):
    """
    Generate a summary of the input text, limited to the specified number of words.
    
    Parameters:
    text (str): The input text.
    max_words (int): The maximum number of words in the summary.
    
    Returns:
    str: A string summary of the text, limited to the specified number of words.
    """

    # Tokenize the text
    tokens = re.findall(r'\b\w+\b', text.lower())

    # Remove stopwords
    stopwords = set(['the', 'and', 'in', 'etc.']) # Add more stopwords as needed
    filtered_tokens = [token for token in tokens if token not in stopwords]

    # Calculate word frequency
    word_freq = defaultdict(int)
    for token in filtered_tokens:
        word_freq[token] += 1

    # Split the text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

    # Score sentences
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in re.findall(r'\b\w+\b', sentence.lower()):
            if word in word_freq:
                sentence_scores[sentence] += word_freq[word]

    # Select top-scoring sentences
    summary_sentences = heapq.nlargest(max_words, sentence_scores, key=sentence_scores.get)

    if len(summary_sentences) == 0:
        return "No summary could be generated."

    # Combine sentences to form the summary
    summary = ' '.join(summary_sentences)
    return summary