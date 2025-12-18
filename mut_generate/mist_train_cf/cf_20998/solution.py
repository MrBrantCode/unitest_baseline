"""
QUESTION:
Write a function named `edit_sentence` that takes a given sentence as input and returns a revised sentence with correct structure, ensuring the resulting sentence does not exceed 15 words.
"""

def edit_sentence(sentence):
    words = sentence.split()
    if len(words) > 15:
        words = words[:15]
    return ' '.join(words).capitalize() + '.'