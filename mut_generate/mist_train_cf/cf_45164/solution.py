"""
QUESTION:
Write a function `accent_frequency(text)` that takes a string of text as input and returns a dictionary where the keys are the accentuated characters present in the text and the values are their corresponding frequencies. The function should treat uppercase and lowercase versions of the same letter as different characters.
"""

import collections

def accent_frequency(text):
    # Define a string of accentuated characters
    accent_chars = "áéíóúÁÉÍÓÚàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛãõÃÕäëïöüÄËÏÖÜçÇ"
    
    # Create a frequency dictionary of the accentuated characters in the text
    freq_dictionary = collections.Counter(c for c in text if c in accent_chars)

    return freq_dictionary