"""
QUESTION:
Create a function named `word_frequency` that takes a list of strings as input and returns a dictionary. The dictionary should have the distinct words as keys and their corresponding values should be another dictionary containing the word's frequency and a list of sentences where the word appears. The word frequency should be case-insensitive, and punctuation should be ignored.
"""

from collections import defaultdict

def word_frequency(sentences):
    """
    Returns a dictionary where keys are distinct words and values are dictionaries 
    containing the word's frequency and a list of sentences where the word appears.

    Args:
        sentences (list): A list of strings.

    Returns:
        dict: A dictionary containing word frequencies and sentences.
    """
    word_dict = defaultdict(lambda: {'count': 0, 'sentences': []})

    for sentence in sentences:
        words = [word.lower().strip('.,?') for word in sentence.split()]
        
        for word in words:
            word_dict[word]['count'] += 1
            if sentence not in word_dict[word]['sentences']:
                word_dict[word]['sentences'].append(sentence)
                
    return dict(word_dict)