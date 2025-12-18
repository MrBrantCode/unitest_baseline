"""
QUESTION:
Write a function called `letter_frequency` that takes a string `sentence` as input and returns a dictionary where the keys are the unique letters in the sentence (in lowercase) and the values are the frequencies of each letter, ignoring punctuation marks and case sensitivity.
"""

def letter_frequency(sentence):
    """
    Calculate the frequency of each letter in the given sentence, ignoring punctuation marks and case sensitivity.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary where the keys are the unique letters in the sentence (in lowercase) and the values are the frequencies of each letter.
    """
    frequency = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1
    return frequency