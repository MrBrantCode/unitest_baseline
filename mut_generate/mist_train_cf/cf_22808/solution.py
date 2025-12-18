"""
QUESTION:
Write a function `calculate_letter_frequency` that calculates the frequency of each letter in a sentence, considering case sensitivity, punctuation marks, and multiple spaces between words. The function should return a list of the letter(s) with the highest frequency in alphabetical order.
"""

def calculate_letter_frequency(sentence):
    """
    Calculate the frequency of each letter in a sentence, 
    considering case sensitivity, punctuation marks, and multiple spaces between words.
    Return a list of the letter(s) with the highest frequency in alphabetical order.

    Args:
    sentence (str): The input sentence.

    Returns:
    list: A list of the letter(s) with the highest frequency in alphabetical order.
    """
    sentence = sentence.lower()
    frequency = {}
    max_frequency = 0

    for char in sentence:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
            max_frequency = max(max_frequency, frequency[char])

    max_letters = [letter for letter, freq in frequency.items() if freq == max_frequency]
    return sorted(max_letters)