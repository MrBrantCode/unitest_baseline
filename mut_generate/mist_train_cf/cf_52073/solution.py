"""
QUESTION:
Design a function `generate_words` that generates a set of five English words starting with the letter "P" and having at least one common substring of length three or more. The generated words must be of different lengths, ranging from 4 to 8 characters long, and sorted by their second character in ascending alphabetical order. The function should have a time complexity better than O(n^2). The input is a list of English words starting with the letter "P".
"""

import re

def generate_words(words):
    """
    Generates a set of five English words starting with the letter "P" and having at least one common substring of length three or more.
    
    Args:
    words (list): A list of English words starting with the letter "P".
    
    Returns:
    list: A list of five words with different lengths, ranging from 4 to 8 characters long, sorted by their second character in ascending alphabetical order.
    """
    words.sort(key=lambda word: len(word)) # Sort by word length

    selected_words = []

    for word in words:
        if len(word) >= 4 and len(word) <= 8: # Check word length
            if len(selected_words) == 0:
                selected_words.append(word)
            elif len(selected_words) < 5 and len(selected_words[-1]) < len(word): # Check different length
                # Check for common substring of 3 characters
                for selected_word in selected_words:
                    if len(set(re.findall('...', selected_word)) & set(re.findall('...', word))) > 0:
                        selected_words.append(word) 
                        break

    # Sort by the second character and return the result
    selected_words.sort(key=lambda word: word[1])
    return selected_words