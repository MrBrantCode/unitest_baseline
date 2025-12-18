"""
QUESTION:
Write a function `calculate_term_proportions(statement)` that calculates the proportion of each distinct term with respect to the aggregate count of terms in a given statement. The function should take a string `statement` as input, split it into words (considering punctuation as word separators), convert the words to lowercase, and return a dictionary where each word is a key and its proportion is its value.
"""

import re
from collections import Counter

def calculate_term_proportions(statement):
    """
    Calculate the proportion of each distinct term with respect to the aggregate count of terms in a given statement.
    
    Parameters:
    statement (str): The input statement.
    
    Returns:
    dict: A dictionary where each word is a key and its proportion is its value.
    """
    # Remove punctuation and convert string to lowercase
    statement = re.sub(r'[.,]', '', statement).lower()
    
    # Tokenize the statement into words
    words = statement.split()
    
    # Create a dictionary where each word is a key and its occurrence is its value
    counts = Counter(words)
    
    # Number of total words
    total_count = sum(counts.values())
    
    # Create a dictionary where each word is a key and its proportion is its value
    proportions = {word: count / total_count for word, count in counts.items()}
    
    return proportions