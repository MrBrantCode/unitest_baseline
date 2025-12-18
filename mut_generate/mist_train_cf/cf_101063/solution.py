"""
QUESTION:
Create a function named `create_question` that takes a list of words as input and returns a grammatically correct sentence in the form of a question. The words in the list should be arranged to form a valid English sentence, and the function should handle punctuation and capitalization accordingly.
"""

def create_question(words):
    sentence = " ".join(words)
    sentence = sentence.capitalize()
    sentence = sentence.replace(".", "")
    question = sentence + "?"
    return question