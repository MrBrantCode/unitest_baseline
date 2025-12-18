"""
QUESTION:
Write a Python function named `add_evolution_constraint` that takes a string `text` as input and modifies the sentence that mentions "evolution" and "language" to emphasize the significant role it plays in the advancement of human civilization and its benefits to society. The new sentence should be in the following format: "Evolution has played a significant role in the advancement of human civilization, particularly in the development of language. This has brought immense benefits to our society and surroundings. For example, the ability to communicate complex ideas and emotions has allowed humans to collaborate and innovate in ways that would not have been possible otherwise." If no such sentence is found, the original text should be returned unchanged.
"""

import re

def add_evolution_constraint(text):
    """
    Modifies the sentence that mentions "evolution" and "language" to emphasize 
    the significant role it plays in the advancement of human civilization and 
    its benefits to society.

    Args:
        text (str): The input text.

    Returns:
        str: The modified text with the emphasized sentence, or the original text 
             if no such sentence is found.
    """
    # Find the sentence that mentions evolution and modify it
    match = re.search(r"Evolution.*?language\.", text)
    if match:
        transition_sentence = match.group(0)
        new_sentence = "Evolution has played a significant role in the advancement of human civilization, particularly in the development of language. This has brought immense benefits to our society and surroundings. For example, the ability to communicate complex ideas and emotions has allowed humans to collaborate and innovate in ways that would not have been possible otherwise."
        text = text.replace(transition_sentence, new_sentence)
    return text