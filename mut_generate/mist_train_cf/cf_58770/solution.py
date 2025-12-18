"""
QUESTION:
Create a function named `assemble_sentence` that takes a list of words as input and returns a sentence. The function should use all the given words to form a grammatically correct sentence, and it can use additional words if necessary to create a coherent sentence.
"""

def assemble_sentence(words):
    """
    Assemble a sentence from a list of words.
    
    Args:
    words (list): A list of words.
    
    Returns:
    str: A grammatically correct sentence using all the given words.
    """
    
    # Initialize the sentence with the first word
    sentence = words[0].capitalize()
    
    # Add the rest of the words to the sentence
    for word in words[1:]:
        # Add a space before each word
        sentence += ' ' + word
    
    # Add a period at the end to complete the sentence
    sentence += '.'
    
    return sentence