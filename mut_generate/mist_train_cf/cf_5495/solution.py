"""
QUESTION:
Write a Python function `calculate_average_word_length(sentence, min_length, include_punctuation)` that takes a string `sentence`, an integer `min_length`, and a boolean `include_punctuation`. The function calculates the average word length and the count of words with a length greater than or equal to `min_length` in the given sentence, with or without considering punctuation marks depending on the value of `include_punctuation`. If the sentence is empty or `min_length` is negative, the function should return `0.0, 0`.
"""

import string

def calculate_average_word_length(sentence, min_length, include_punctuation):
    # Check if the sentence is empty or minimum length is negative
    if not sentence or min_length < 0:
        return 0.0, 0
    
    # Remove punctuation marks if include_punctuation is False
    if not include_punctuation:
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    words = sentence.split()
    total_length = 0
    count = 0
    
    for word in words:
        # Check if word length meets the specified minimum length
        if len(word) >= min_length:
            total_length += len(word)
            count += 1
    
    if count == 0:
        return 0.0, 0
    
    average_length = total_length / count
    return average_length, count