"""
QUESTION:
Write a Python function `classify_sentence` that takes a string `sentence` as input and returns the type of sentence (statement, question, command, or exclamation) based on its punctuation. Assume that a sentence ending with '?' is a question, '.' is a statement, '!' is an exclamation, and any other punctuation is a command. The function should remove any leading or trailing whitespace and ignore any punctuation marks within the sentence.
"""

def classify_sentence(sentence):
    """
    Classify the type of sentence based on its punctuation.

    Args:
    sentence (str): The input sentence.

    Returns:
    str: The type of sentence (statement, question, command, or exclamation).
    """
    sentence = sentence.strip()  # Remove leading/trailing whitespace
    last_char = sentence[-1]  # Get the last character of the sentence

    if last_char == '?':
        return "question"
    elif last_char == '.':
        return "statement"
    elif last_char == '!':
        return "exclamation"
    else:
        return "command"