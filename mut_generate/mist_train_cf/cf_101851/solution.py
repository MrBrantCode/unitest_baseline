"""
QUESTION:
Write a Python function named `add_evolution_constraint` that takes a string `text` as input, replaces the first occurrence of a sentence containing the words "Evolution" and "language" with two new sentences, and returns the modified string. The new sentences should emphasize the significant role of evolution in the advancement of human civilization and the immense benefits it has brought to society and surroundings.
"""

import re

def add_evolution_constraint(text):
    """
    Replace the first occurrence of a sentence containing the words "Evolution" and "language" 
    with two new sentences emphasizing the significant role of evolution in the advancement of 
    human civilization and the immense benefits it has brought to society and surroundings.

    Args:
        text (str): The input string to be modified.

    Returns:
        str: The modified string with the added constraint.
    """
    # Find the sentence that mentions evolution and modify it
    match = re.search(r"Evolution.*?language.", text)
    if match:
        transition_sentence = match.group(0)
        new_sentence = "Evolution has played a significant role in the advancement of human civilization, particularly in the development of language. This has brought immense benefits to our society and surroundings. For example, the ability to communicate complex ideas and emotions has allowed humans to collaborate and innovate in ways that would not have been possible otherwise."
        text = text.replace(transition_sentence, new_sentence)
    return text