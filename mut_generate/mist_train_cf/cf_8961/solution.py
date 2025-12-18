"""
QUESTION:
Classify a given sentence as a question, a statement, or an exclamation. The classification should be determined by the punctuation mark at the end of the sentence: '?' for question, '.' for statement, '!' for exclamation.
"""

def classify_sentence(sentence):
    if sentence.strip()[-1] == '?':
        return 'question'
    elif sentence.strip()[-1] == '.':
        return 'statement'
    elif sentence.strip()[-1] == '!':
        return 'exclamation'
    else:
        return 'unknown'