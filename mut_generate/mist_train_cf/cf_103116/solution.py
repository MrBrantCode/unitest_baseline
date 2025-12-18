"""
QUESTION:
Write a function `find_phrase_frequency` that takes two parameters: `text` and `phrase`. The function should return the frequency of the given phrase in the text, considering both case sensitivity and punctuation marks. The function should be able to count phrases separated by punctuation marks as separate occurrences.
"""

def find_phrase_frequency(text, phrase):
    """
    This function calculates the frequency of a given phrase in a text, 
    considering case sensitivity and punctuation marks.

    Args:
        text (str): The input text.
        phrase (str): The phrase to be searched.

    Returns:
        int: The frequency of the phrase in the text.
    """
    import re
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation marks
    words = text.split()  # Split the text into words
    phrase_words = phrase.split()  # Split the phrase into words
    phrase_length = len(phrase_words)  # Get the length of the phrase
    frequency = 0  # Initialize the frequency counter
    for i in range(len(words) - phrase_length + 1):  # Iterate over the text
        if ' '.join(words[i:i + phrase_length]) == phrase:  # Check if the phrase matches
            frequency += 1  # Increment the frequency counter
    return frequency