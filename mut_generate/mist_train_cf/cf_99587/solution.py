"""
QUESTION:
Write a function called rewrite_sentence that takes a sentence as input and returns a rewritten sentence with the following changes: 
1. The verb "consumed" is replaced with "eats", and "proceeded" is replaced with "starts".
2. The pronoun "their" is replaced with "his or her".
3. The sentence ends with a period.
"""

def rewrite_sentence(sentence):
    """
    Rewrites a sentence by replacing "consumed" with "eats", "proceeded" with "starts", 
    "their" with "his or her", and appends a period at the end.

    Args:
        sentence (str): The input sentence to be rewritten.

    Returns:
        str: The rewritten sentence.
    """
    return sentence.replace("consumed", "eats").replace("proceeded", "starts").replace("their", "his or her") + "."