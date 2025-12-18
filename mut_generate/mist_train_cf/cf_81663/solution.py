"""
QUESTION:
Create a function `analyze_frequency(message)` that takes a string as input, converts it to lowercase, removes non-alphabetic characters, and returns a dictionary where the keys are the alphabetic characters from the input string and the values are their corresponding frequencies.
"""

def analyze_frequency(message):
    """
    Analyzes the frequency of alphabetic characters in a given message.

    Args:
        message (str): The input string to be analyzed.

    Returns:
        dict: A dictionary where keys are the alphabetic characters and values are their frequencies.
    """
    message = message.lower()
    frequency = dict()
    for letter in message:
        if letter.isalpha():
            if letter not in frequency:
                frequency[letter] = 1
            else:
                frequency[letter] += 1
    return frequency