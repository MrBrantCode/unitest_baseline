"""
QUESTION:
Write a function `calculate_average_word_length(sentence, min_length)` that calculates the average word length in a given sentence and counts the number of words that have a length greater than or equal to a specified value. 

The function should take two arguments: a string `sentence` and an integer `min_length` representing the minimum length of words to consider. 

The function should return a tuple containing two values: a float representing the average word length and an integer representing the count of words that meet the specified minimum length. 

The function should handle cases where the sentence is empty or the minimum length is negative, and return `None` in such cases.
"""

def entance(sentence, min_length):
    if len(sentence) == 0 or min_length < 0:
        return None

    words = sentence.split()
    word_count = 0
    total_length = 0

    for word in words:
        if len(word) >= min_length:
            word_count += 1
            total_length += len(word)

    average_length = total_length / word_count if word_count > 0 else 0

    return average_length, word_count