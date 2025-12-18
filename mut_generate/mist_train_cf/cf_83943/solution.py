"""
QUESTION:
Write a function named `count_terms` that takes a string input `narrative` and returns a dictionary where the keys are unique terms and the values are their respective counts. The function should be case-insensitive and consider 'The' and 'the' as the same term. It should not distinguish between different forms of the same term. Use regular expressions to extract terms from the input string.
"""

import re
from collections import Counter

def count_terms(narrative):
    """
    Returns a dictionary where the keys are unique terms in the narrative
    and the values are their respective counts.

    The function is case-insensitive and considers different forms of
    the same term as the same term.

    :param narrative: The input string
    :return: A dictionary of term counts
    """
    terms = re.findall(r'\b\w+\b', narrative.lower())
    return Counter(terms)