"""
QUESTION:
Write a function called `classify_sentence` that takes a sentence as input and classifies it as declarative, interrogative, exclamatory, or imperative based on its punctuation. The classification should be determined by the last character of the sentence: period (`.`) for declarative, question mark (`?`) for interrogative, exclamation mark (`!`) for exclamatory. Imperative sentences can end with a period, question mark, or exclamation mark, but this classification should only be considered if the sentence does not fit into any other category. If the sentence does not fit any of the above categories, return 'Unknown'.
"""

def classify_sentence(sentence):
    if sentence.endswith('.'):
        return 'Declarative'
    elif sentence.endswith('?'):
        return 'Interrogative'
    elif sentence.endswith('!'):
        return 'Exclamatory'
    elif sentence.endswith('!') or sentence.endswith('.') or sentence.endswith('?'):
        return 'Imperative'
    else:
        return 'Unknown'