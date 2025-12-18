"""
QUESTION:
Write a function `add_evolution_constraint` that takes a string of text as input and returns the modified text with a transition sentence regarding the importance of evolution in human language development. The transition sentence should emphasize the significant role it plays in the advancement of human civilization, followed by an additional sentence that highlights the immense benefits it has brought to our society and surroundings.
"""

import re

def add_evolution_constraint(text):
    # Find the sentence that mentions evolution and modify it
    match = re.search(r"Evolution.*?language.", text)
    if match:
        transition_sentence = match.group(0)
        new_sentence = "Evolution has played a significant role in the advancement of human civilization, particularly in the development of language. This has brought immense benefits to our society and surroundings. For example, the ability to communicate complex ideas and emotions has allowed humans to collaborate and innovate in ways that would not have been possible otherwise."
        text = text.replace(transition_sentence, new_sentence)
    return text