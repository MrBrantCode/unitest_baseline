"""
QUESTION:
Write a function named `longest_word(sentence)` that takes a sentence as input, returns or prints the longest word excluding words containing digits or special characters, and prioritizes the first occurrence in case of multiple longest words. The input sentence will only contain spaces as word separators.
"""

def longest_word(sentence):
    """Return the longest word in a sentence, excluding words containing digits or special characters.
    
    In case of multiple longest words, prioritize the first occurrence.
    
    Args:
    sentence (str): The input sentence containing only spaces as word separators.
    
    Returns:
    str: The longest word in the sentence.
    """
    words = sentence.split()
    longest = ""
    for word in words:
        # Check if the word is alphanumeric
        if word.isalpha():
            if len(word) > len(longest):
                longest = word
    return longest