"""
QUESTION:
Write a function named `count_thesaurus_frequency` that takes a dictionary `thesaurus` and a string `text` as input. The function should return the frequency of each phrase in the thesaurus and its corresponding expressions in the text. The function should be case-insensitive and should ignore punctuation. The thesaurus dictionary has phrases as keys and lists of expressions as values.
"""

from collections import Counter
import string

def count_thesaurus_frequency(thesaurus, text):
    """
    Returns the frequency of each phrase in the thesaurus and its corresponding expressions in the text.

    Args:
    thesaurus (dict): A dictionary with phrases as keys and lists of expressions as values.
    text (str): The input text.

    Returns:
    dict: A dictionary with phrases and expressions as keys and their frequencies as values.
    """
    
    # Prepare the text: remove punctuation, lower case, and split into words
    words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()

    # The counter
    counter = Counter()

    # Count the phrases and expressions
    for phrase, expressions in thesaurus.items():
        # Count the phrase
        counter[phrase] += words.count(phrase)

        # Count the expressions
        for expression in expressions: 
            counter[expression] += words.count(expression)

    return dict(counter)