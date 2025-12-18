"""
QUESTION:
Classify the sentences in the given text into their respective types. Implement a function `classify_sentence` that takes a sentence as input and returns its type. The function should categorize the sentences into declarative, interrogative, exclamatory, or imperative. The input text will contain only sentences that end with a period (.), question mark (?), or exclamation mark (!).
"""

def classify_sentence(sentence):
    """
    Classify a sentence into its type: declarative, interrogative, exclamatory, or imperative.

    Args:
    sentence (str): The input sentence to be classified.

    Returns:
    str: The type of the sentence.
    """
    if sentence.strip()[-1] == '.':
        return "declarative"
    elif sentence.strip()[-1] == '?':
        return "interrogative"
    elif sentence.strip()[-1] == '!':
        return "exclamatory"
    else:
        return "imperative"