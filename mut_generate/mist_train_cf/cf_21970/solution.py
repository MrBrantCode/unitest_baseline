"""
QUESTION:
Write a function called `process_sentence` that takes a string input containing a sentence. The function should remove all white spaces from the sentence, count the number of words in the original sentence, and reverse the sentence while preserving punctuation marks and special characters. Return the reversed sentence and the word count.
"""

def process_sentence(sentence):
    """
    This function processes a sentence by removing white spaces, counting the number of words, 
    and reversing the sentence while preserving punctuation marks and special characters.

    Args:
        sentence (str): The input sentence to be processed.

    Returns:
        tuple: A tuple containing the reversed sentence and the word count.
    """
    # Removing white space
    sentence_no_space = sentence.replace(" ", "")

    # Counting number of words
    num_words = len(sentence.split())

    # Reversing the sentence
    reversed_sentence = sentence_no_space[::-1]

    return reversed_sentence, num_words