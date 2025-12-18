"""
QUESTION:
Write a function `capitalize_sentence` that takes a string of words as input and returns the string with the first letter of each word capitalized. The input string is separated by spaces, and the output should also be separated by spaces.
"""

def capitalize_sentence(sentence):
    """
    Capitalize the first letter of each word in a sentence.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        str: The sentence with the first letter of each word capitalized.
    """
    # split the sentence into individual words, capitalize each word, and join them back together
    return " ".join(word.capitalize() for word in sentence.split(" "))