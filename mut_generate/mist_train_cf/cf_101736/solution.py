"""
QUESTION:
Write a Python function named `emphasize_evolution` that takes a string `text` as input, replaces the first sentence that mentions "evolution" and "language" with a new sentence emphasizing the significant role of evolution in the advancement of human civilization, particularly in the development of language, and returns the modified text. The new sentence should also highlight the immense benefits it has brought to society and surroundings.
"""

import re

def emphasize_evolution(text):
    """
    This function replaces the first sentence that mentions "evolution" and "language" 
    with a new sentence emphasizing the significant role of evolution in the advancement 
    of human civilization, particularly in the development of language, and returns 
    the modified text.
    
    Args:
        text (str): The input text that may or may not contain a sentence with "evolution" and "language".
    
    Returns:
        str: The modified text with the new sentence added if a sentence with "evolution" and "language" is found.
    """

    # Find the sentence that mentions evolution and modify it
    match = re.search(r"Evolution.*?language.", text)
    if match:
        transition_sentence = match.group(0)
        new_sentence = "Evolution has played a significant role in the advancement of human civilization, particularly in the development of language. This has brought immense benefits to our society and surroundings. For example, the ability to communicate complex ideas and emotions has allowed humans to collaborate and innovate in ways that would not have been possible otherwise."
        text = text.replace(transition_sentence, new_sentence)
    return text