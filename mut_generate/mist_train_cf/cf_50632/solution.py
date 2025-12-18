"""
QUESTION:
Create a function `word_freq(text, word)` that determines the frequency of a specific word within a provided text passage. The function should work regardless of letter case and presence of punctuation in the text passage. If the word is not provided, the function should include error handling to handle this case.
"""

import string

def word_freq(text, word):
    try:
        # Remove punctuations and convert to lower case
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        word = word.lower()

        # Split the words in the text
        words = text.split()

        # Return the count of word in words
        return words.count(word)
    except Exception as e:
        return "Error: " + str(e)