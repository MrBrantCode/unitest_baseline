"""
QUESTION:
Write a Python function `calculate_weightage` to classify each sentence in a paragraph into "optimistic" or "pessimistic" based on the presence of optimistic or pessimistic words. The function should calculate the weightage of each word based on its position and frequency in the sentence, and use a dictionary to store the words and their corresponding sentiment score. 

The function should take a sentence as input, extract all words from the sentence, weight each word based on its position, and update the sentiment score of the word in the dictionary. The function should then return the weightage of the sentence.

Assume that the list of optimistic and pessimistic words are predefined as `optimistic_words` and `pessimistic_words`, respectively. The dictionary to store the words and their corresponding sentiment score is `sentiment_scores`.
"""

import re

def calculate_weightage(sentence, optimistic_words, pessimistic_words, sentiment_scores):
    """
    Calculate the weightage of a sentence based on the presence of optimistic and pessimistic words.
    
    Parameters:
    sentence (str): The sentence to be classified.
    optimistic_words (list): A list of optimistic words.
    pessimistic_words (list): A list of pessimistic words.
    sentiment_scores (dict): A dictionary to store the words and their corresponding sentiment score.
    
    Returns:
    float: The weightage of the sentence.
    """
    words = re.findall(r'\b\w+\b', sentence)  # Extract all words from the sentence
    weightage = 0
    for i, word in enumerate(words):
        if word in optimistic_words:
            weightage += (len(words) - i) / len(words)  # Weight the word based on its position
            if word in sentiment_scores:
                sentiment_scores[word] += weightage  # Update the sentiment score of the word
            else:
                sentiment_scores[word] = weightage  # Add the word to the dictionary with its sentiment score
        elif word in pessimistic_words:
            weightage -= (len(words) - i) / len(words)  # Weight the word based on its position
            if word in sentiment_scores:
                sentiment_scores[word] += weightage  # Update the sentiment score of the word
            else:
                sentiment_scores[word] = weightage  # Add the word to the dictionary with its sentiment score
    return weightage