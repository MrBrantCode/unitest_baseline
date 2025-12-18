"""
QUESTION:
Write a function named `reverse_sentence` that takes a string of words as input and returns a string with the words in reverse order, without reversing the letters in each word. The input string may contain multiple words separated by spaces.
"""

def reverse_sentence(sentence):
    """
    This function takes a string of words as input and returns a string 
    with the words in reverse order, without reversing the letters in each word.

    Args:
        sentence (str): The input string of words.

    Returns:
        str: A string with the words in reverse order.
    """
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence