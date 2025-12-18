"""
QUESTION:
Write a function named `determine_sentence_type` that takes a sentence as a string and returns the type of the sentence, either "question" or "statement". The function should determine the type based on the presence or absence of a question mark at the end of the sentence.
"""

def determine_sentence_type(sentence):
    if sentence[-1] == '?':
        return 'question'
    else:
        return 'statement'