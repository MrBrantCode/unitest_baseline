"""
QUESTION:
Write a function `classify_word` that takes a word as input and classifies it as an adverb if it ends with "ly".
"""

def classify_word(word):
    if word.endswith("ly"):
        return f"{word} is an adverb"
    else:
        return f"{word} is not an adverb"