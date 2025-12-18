"""
QUESTION:
Develop a function named `identify_questions` that takes a sentence as input and identifies whether it is a question or not. The function should return True if the sentence is a question and False otherwise. The function should handle various question formats and punctuation marks.
"""

def identify_questions(sentence):
    """
    This function identifies whether a given sentence is a question or not.

    Args:
        sentence (str): The input sentence to be evaluated.

    Returns:
        bool: True if the sentence is a question, False otherwise.
    """
    # Remove leading and trailing whitespaces from the sentence
    sentence = sentence.strip()
    
    # Check if the sentence ends with a question mark
    # or has a question word at the beginning
    question_words = ["what", "where", "when", "who", "why", "how"]
    sentence = sentence.lower()
    return sentence.endswith("?") or any(sentence.startswith(word) for word in question_words)