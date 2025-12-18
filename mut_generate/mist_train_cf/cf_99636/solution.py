"""
QUESTION:
Create a function named `determine_sentence_type` that takes a sentence as a string and determines whether it is a statement or a question. The function should output "statement" if the sentence is a statement and "question" if the sentence is a question. The sentence type can be determined by the presence of a question mark at the end of the sentence.
"""

def determine_sentence_type(sentence):
    if sentence.strip()[-1] == '?':
        return 'question'
    else:
        return 'statement'