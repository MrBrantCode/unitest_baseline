"""
QUESTION:
Create a function named 'reverse_sentence' that takes a sentence as a string and returns the sentence with the words in reverse order. The function should not change the order of characters within each word, only reverse the order of words in the sentence. The input sentence may contain multiple spaces between words.
"""

def reverse_sentence(sentence):
    """
    This function takes a sentence as a string and returns the sentence with the words in reverse order.
    
    Args:
        sentence (str): The input sentence.
    
    Returns:
        str: The sentence with the words in reverse order.
    """
    words = sentence.split()
    return ' '.join(reversed(words))