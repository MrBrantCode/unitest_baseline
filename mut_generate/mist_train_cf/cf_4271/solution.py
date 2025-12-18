"""
QUESTION:
Reverse the words in a given sentence while maintaining the original punctuation marks and capitalization. Implement a function called `reverse_words` that takes a string as input and returns the reversed sentence. The function should handle punctuation marks as part of the word they are attached to, and the first letter of the first word in the reversed sentence should be capitalized, while the rest of the letters should be in lowercase.
"""

def reverse_words(sentence):
    """
    Reverses the words in a given sentence while maintaining the original punctuation marks and capitalization.
    
    Args:
        sentence (str): The input sentence to be reversed.
    
    Returns:
        str: The reversed sentence.
    """
    # Split the sentence into words and punctuation
    words = sentence.split()
    
    # Reverse the order of the words
    reversed_words = words[::-1]
    
    # Reconstruct the sentence with the reversed words
    reversed_sentence = ' '.join(reversed_words)
    
    # Convert the sentence to lowercase and capitalize the first letter
    reversed_sentence = reversed_sentence.lower()
    if len(reversed_sentence) > 0:
        reversed_sentence = reversed_sentence[0].upper() + reversed_sentence[1:]
    
    return reversed_sentence