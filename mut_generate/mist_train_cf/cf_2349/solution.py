"""
QUESTION:
Write a function `count_vowels` that takes a string `sentence` as input and returns a dictionary where the keys are the vowels in the sentence and the values are their respective counts. The function should ignore non-alphabetic characters and exclude any vowels that are immediately preceded or followed by another vowel. The function should also consider the input string in lowercase.
"""

import re
from collections import Counter

def count_vowels(sentence):
    """
    This function takes a string sentence as input and returns a dictionary where the keys are the vowels in the sentence 
    and the values are their respective counts. The function ignores non-alphabetic characters and excludes any vowels that 
    are immediately preceded or followed by another vowel. The function considers the input string in lowercase.

    Parameters:
    sentence (str): The input string

    Returns:
    dict: A dictionary where the keys are the vowels and the values are their counts
    """
    # Convert the sentence to lowercase
    sentence = sentence.lower()

    # Remove non-alphabetic characters
    sentence = re.sub(r'[^a-z\s]', '', sentence)

    # Find all vowels
    vowels = re.findall(r'[aeiou]', sentence)

    # Exclude vowels that are immediately preceded or followed by another vowel
    filtered_vowels = []
    for i in range(len(vowels)):
        if i == 0 or vowels[i] != vowels[i-1]:
            if i == len(vowels)-1 or vowels[i] != vowels[i+1]:
                filtered_vowels.append(vowels[i])

    # Count the occurrences of each vowel
    vowel_counts = Counter(filtered_vowels)

    return vowel_counts