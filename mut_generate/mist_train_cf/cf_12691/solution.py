"""
QUESTION:
Write a function called `find_longest_sentence` that takes a list of sentences as input and returns the longest sentence. The input list should contain no more than 100 words. The function should exclude any sentences that contain numbers or special characters.
"""

import re

def find_longest_sentence(sentences):
    longest_sentence = ""
    max_length = 0

    for sentence in sentences:
        # Exclude sentences with numbers or special characters
        if re.search(r'[0-9!@#$%^&*(),.?":{}|<>]', sentence):
            continue

        # Calculate the length of the sentence
        length = len(sentence.split())

        # Update the longest sentence if necessary
        if length > max_length:
            max_length = length
            longest_sentence = sentence

    return longest_sentence