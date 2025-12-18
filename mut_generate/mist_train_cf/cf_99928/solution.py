"""
QUESTION:
Write a function `emphasize_evolution` that takes a string `text` as input, finds the first sentence that mentions "evolution" followed by "language", and replaces it with two new sentences that emphasize the significant role of evolution in human civilization and its benefits to society. The new sentences should be "Evolution has played a significant role in the advancement of human civilization, particularly in the development of language." and "This has brought immense benefits to our society and surroundings."
"""

import re

def emphasize_evolution(text):
    """
    This function finds the first sentence that mentions "evolution" followed by "language" 
    in the given text and replaces it with two new sentences that emphasize the significant 
    role of evolution in human civilization and its benefits to society.

    Args:
        text (str): The input text to be modified.

    Returns:
        str: The modified text.
    """
    match = re.search(r"Evolution.*?language.", text)
    if match:
        transition_sentence = match.group(0)
        new_sentence = "Evolution has played a significant role in the advancement of human civilization, particularly in the development of language. This has brought immense benefits to our society and surroundings."
        text = text.replace(transition_sentence, new_sentence)
    return text