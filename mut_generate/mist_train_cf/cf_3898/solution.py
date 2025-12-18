"""
QUESTION:
Write a function named `most_frequent_letter` that takes a string `sentence` as input and returns the most frequent letter in the sentence. The function should ignore any special characters or digits, exclude any letters that appear more than once consecutively and are followed by a vowel, and handle uppercase and lowercase letters as separate entities. The input string can be up to 100 characters long.
"""

import re

def most_frequent_letter(sentence):
    # Remove special characters and digits
    sentence = re.sub('[^a-zA-Z ]+', '', sentence)
    
    # Initialize a dictionary to store letter frequencies
    frequencies = {}
    
    # Iterate through each letter in the sentence
    for i in range(len(sentence)):
        letter = sentence[i]
        
        # Ignore consecutive letters followed by a vowel
        if i > 0 and sentence[i-1] == letter and i < len(sentence) - 1 and sentence[i+1] in 'aeiou':
            continue
        
        # Increment the frequency of the letter
        frequencies[letter] = frequencies.get(letter, 0) + 1
    
    # Find the most frequent letter
    most_frequent = max(frequencies, key=frequencies.get)
    
    return most_frequent