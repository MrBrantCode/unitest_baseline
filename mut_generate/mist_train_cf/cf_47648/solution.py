"""
QUESTION:
Given a character sequence with hyphens as delimiters, write a function `calculate_frequency` that calculates and returns the frequencies of each unique word in the sequence. The function should consider case sensitivity and handle edge cases such as multiple consecutive delimiters and trailing/leading delimiters. The input is a string and the output should be a dictionary where keys are unique words and values are their corresponding frequencies.
"""

def calculate_frequency(character_sequence):
    # Split the sequence at hyphens and ignore any empty resulting words
    words = [word for word in character_sequence.split('-') if word]

    # Store frequencies in a dictionary
    frequencies = {}

    # Calculate frequencies
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies