"""
QUESTION:
Create a function named `word_count` that utilizes regular expressions to tally the instances of each distinct term found within a given narrative text block. The function should take a string as input, convert it to lowercase, split it into words using regular expressions, and return a dictionary where the keys are the distinct words and the values are their corresponding counts.
"""

import re
from collections import Counter

def word_count(narrative):
    """
    This function takes a string as input, converts it to lowercase, 
    splits it into words using regular expressions, and returns a dictionary 
    where the keys are the distinct words and the values are their corresponding counts.

    Args:
        narrative (str): The input text block.

    Returns:
        dict: A dictionary containing word counts.
    """
    words = re.findall(r'\w+', narrative.lower())
    return dict(Counter(words))