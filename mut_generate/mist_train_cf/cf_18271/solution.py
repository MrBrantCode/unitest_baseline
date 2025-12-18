"""
QUESTION:
Implement a function `match_quantifier` that takes a string pattern and an input string as parameters and returns a tuple containing the matched string and the type of quantifier used. The function should support both greedy and lazy quantifiers. The pattern should contain either '+' (greedy) or '+?' (lazy) as the quantifier.
"""

import re

def match_quantifier(pattern, input_string):
    """
    This function takes a string pattern and an input string as parameters and returns a tuple containing the matched string and the type of quantifier used.
    
    Parameters:
    pattern (str): The regular expression pattern to be matched. It should contain either '+' (greedy) or '+?' (lazy) as the quantifier.
    input_string (str): The input string to be matched against the pattern.
    
    Returns:
    tuple: A tuple containing the matched string and the type of quantifier used.
    """

    # Check if the pattern contains a greedy or lazy quantifier
    if '+?' in pattern:
        # If the pattern contains a lazy quantifier, use a non-greedy regex match
        match = re.search(pattern.replace('+?', '+'), input_string)
        quantifier_type = 'lazy'
    elif '+' in pattern:
        # If the pattern contains a greedy quantifier, use a greedy regex match
        match = re.search(pattern, input_string)
        quantifier_type = 'greedy'
    else:
        # If the pattern does not contain a '+' or '+?' quantifier, return an empty tuple
        return ("", "")

    # If a match is found, return the matched string and the type of quantifier used
    if match:
        return (match.group(), quantifier_type)
    else:
        # If no match is found, return an empty tuple
        return ("", "")