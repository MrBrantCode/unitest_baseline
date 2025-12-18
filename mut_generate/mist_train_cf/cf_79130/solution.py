"""
QUESTION:
Write a function `word_frequency(word, string_list)` that calculates the frequency and frequency rate of a given word within a list of strings. The function should be case-insensitive and should count the word regardless of its position in the sentence and punctuation. The function should return the total count of the word and its frequency rate in the list of strings. The frequency rate is calculated by dividing the total count of the word by the number of strings in the list.
"""

import re

def word_frequency(word, string_list):
    # Initiate count
    count = 0

    # Convert word to lowercase for accurate comparison
    word = word.lower()

    # Iterate over each string in the list
    for string in string_list:
        # Lowercase the string, remove punctuation, and split it into separate words
        words = re.findall(r'\b\w+\b', string.lower())
        
        # Increase count for each occurrence of the word in the string
        count += words.count(word)
        
    frequency_rate = count/len(string_list)

    return count, frequency_rate