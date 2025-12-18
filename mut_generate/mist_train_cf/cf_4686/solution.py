"""
QUESTION:
Classify a sentence as either a declaration or an instruction. The classification should be able to handle sentences with multiple clauses and punctuation marks, including nested clauses and punctuation marks like parentheses, semicolons, and colons. Create a function called `classify_sentence` that takes a sentence as input and returns the classification.
"""

def classify_sentence(sentence):
    sentence = sentence.strip()
    if sentence.endswith('?'):
        return 'instruction'
    if sentence.endswith('.'):
        if any(char in sentence for char in ['(', ')', ':', ';']):
            return 'instruction'
        else:
            return 'declaration'
    else:
        return 'instruction'