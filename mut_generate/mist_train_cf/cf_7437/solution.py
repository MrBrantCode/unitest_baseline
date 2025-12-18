"""
QUESTION:
Create a recursive function `process_sentence` that takes a string as input, removes all white spaces, and returns the reversed sentence along with the total number of words in the sentence. The function should handle punctuation marks and special characters. The input string can contain extra white spaces, punctuations, special characters, and nested parentheses.
"""

def process_sentence(sentence):
    """
    This function takes a string as input, removes all white spaces, 
    and returns the reversed sentence along with the total number of words in the sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: A tuple containing the reversed sentence and the total number of words.
    """

    # Remove white spaces and punctuation marks
    sentence = ''.join(e for e in sentence if e.isalnum() or e.isspace())

    # Remove leading and trailing white spaces
    sentence = sentence.strip()

    # Split the sentence into words
    words = sentence.split()

    # Count the number of words
    num_words = len(words)

    # Reverse the sentence
    reversed_sentence = ' '.join(reversed(words))

    return reversed_sentence, num_words