"""
QUESTION:
Write a function `remove_punctuation` that takes a sentence as input and returns the sentence with all punctuations removed and all letters converted to lowercase. If the sentence contains any numbers, replace the numbers with their corresponding word representation.
"""

import re

def remove_punctuation(sentence):
    """
    This function removes punctuation from a sentence, converts it to lowercase, 
    and replaces numbers with their word representation.

    Parameters:
    sentence (str): The input sentence.

    Returns:
    str: The sentence with punctuation removed, in lowercase, and numbers replaced.
    """
    
    # Define a dictionary to map numbers to their word representation
    number_words = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"
    }

    # Remove punctuation from the sentence
    sentence = re.sub(r'[^\w\s]', '', sentence)

    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Split the sentence into words
    words = sentence.split()

    # Replace numbers with their word representation
    words = [number_words.get(word, word) for word in words]

    # Join the words back into a sentence
    return " ".join(words)