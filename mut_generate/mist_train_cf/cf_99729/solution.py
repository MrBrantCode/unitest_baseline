"""
QUESTION:
Write a function named word_count that takes a string sentence as input and returns a dictionary where the keys are the unique words in the sentence and the values are the number of occurrences of each word. The function should consider words as case-sensitive and include punctuation as part of the word.
"""

def word_count(sentence):
    """
    This function takes a string sentence as input and returns a dictionary where 
    the keys are the unique words in the sentence and the values are the number 
    of occurrences of each word. The function considers words as case-sensitive 
    and includes punctuation as part of the word.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary where the keys are the unique words and the values are 
        the number of occurrences of each word.
    """
    words = sentence.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts