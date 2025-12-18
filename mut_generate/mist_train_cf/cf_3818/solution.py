"""
QUESTION:
Write a function `longest_word(sentence)` that returns the longest word in a given sentence, excluding any words that contain both the letter 'a' and the letter 'b', and with a minimum length of 5 characters.
"""

def longest_word(sentence):
    """
    Returns the longest word in a sentence, excluding any words that contain both the letter 'a' and the letter 'b', 
    and with a minimum length of 5 characters.

    Args:
    sentence (str): The input sentence.

    Returns:
    str: The longest word in the sentence that meets the criteria.
    """
    words = sentence.split()
    longest = ""
    for word in words:
        if 'a' in word and 'b' in word:
            continue
        if len(word) >= 5 and len(word) > len(longest):
            longest = word
    return longest