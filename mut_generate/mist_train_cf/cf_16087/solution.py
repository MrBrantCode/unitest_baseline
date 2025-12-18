"""
QUESTION:
Create a function called `detectOffensiveWords` that takes two parameters: `sentence` (string) and `offensiveWords` (list of strings). The function should return True if the sentence contains any words or phrases from the offensiveWords list, ignoring variations in capitalization and punctuation. The function should also handle special characters in the offensive words and phrases, and it should not require any additional inputs other than the sentence and the list of offensive words.
"""

import re

def detectOffensiveWords(sentence, offensiveWords):
    """
    This function checks if a given sentence contains any offensive words or phrases.

    Parameters:
    sentence (str): The input sentence to be checked.
    offensiveWords (list): A list of offensive words or phrases.

    Returns:
    bool: True if the sentence contains any offensive words or phrases, False otherwise.
    """

    # Convert the sentence to lowercase
    lowercaseSentence = sentence.lower()

    # Remove punctuation marks from the sentence
    cleanedSentence = re.sub(r'[^\w\s]', '', lowercaseSentence)

    # Split the sentence into individual words
    words = cleanedSentence.split()

    # Iterate through each word in the sentence
    for word in words:
        # Remove special characters from the word
        cleanedWord = re.sub(r'[^a-zA-Z0-9]', '', word)
        
        # Check if the word is in the list of offensive words
        if cleanedWord in [re.sub(r'[^a-zA-Z0-9]', '', x.lower()) for x in offensiveWords]:
            return True

    # Check if the entire sentence is in the list of offensive words
    if cleanedSentence in [re.sub(r'[^a-zA-Z0-9]', '', x.lower()) for x in offensiveWords]:
        return True

    return False