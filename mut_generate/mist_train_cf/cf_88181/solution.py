"""
QUESTION:
Write a function named `classify_word` that classifies a given word as a noun, verb, or adjective based on the following rules:
- If a word starts with a capital letter and ends with "ing", classify it as a verb.
- If a word starts with a lowercase letter and ends with "ing", classify it as an adjective.
- If a word starts with a capital letter and ends with "ed", classify it as a noun.
- If a word starts with a lowercase letter and ends with "ed", classify it as a verb.
- If a word starts with a capital letter and has more than two syllables, classify it as a noun.
- If a word starts with a lowercase letter and has more than two syllables, classify it as a verb.
- If a word starts with a lowercase letter and ends with "y", classify it as an adjective.
"""

def classify_word(word):
    if word[0].isupper():
        if word.endswith("ing"):
            return "verb"
        elif word.endswith("ed") or len(word.split()) > 2:
            return "noun"
    else:
        if word.endswith("ing"):
            return "adjective"
        elif word.endswith("ed"):
            return "verb"
        elif word.endswith("y"):
            return "adjective"

    return "unknown"