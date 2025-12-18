"""
QUESTION:
Classify a given sentence as either a statement or a question. 

Write a function classify_sentence(sentence) that takes a string as input and returns 'statement' if the sentence is a statement and 'question' if it is a question.
"""

def classify_sentence(sentence):
    """
    Classify a given sentence as either a statement or a question.
    
    Args:
        sentence (str): The input sentence to be classified.
    
    Returns:
        str: 'statement' if the sentence is a statement, 'question' if it's a question.
    """
    sentence = sentence.strip()  # Remove leading/trailing spaces
    if sentence.endswith('?'):
        return 'question'
    else:
        return 'statement'