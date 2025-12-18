"""
QUESTION:
Calculate the average word length in a given sentence and count the number of words that have a length greater than or equal to a specified value. 

Create a function called `calculate_average_word_length` that takes a string `sentence`, an integer `min_length`, and a boolean `include_punctuation` as arguments. 

If `include_punctuation` is False, exclude punctuation marks from the word length calculation. Handle cases where the `sentence` is empty or `min_length` is negative.

The function should return a tuple containing two values: a float representing the average word length, and an integer representing the count of words that meet the specified minimum length.
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