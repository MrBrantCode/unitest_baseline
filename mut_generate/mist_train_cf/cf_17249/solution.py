"""
QUESTION:
Write a function `count_vowels` that takes a string `sentence` as input, where the sentence only contains lowercase letters and spaces. The function should count the occurrences of each vowel in the sentence, excluding any vowels that are immediately preceded or followed by another vowel, and return a dictionary with the vowel counts.
"""

def count_vowels(sentence):
    """
    Counts the occurrences of each vowel in the sentence, excluding any vowels 
    that are immediately preceded or followed by another vowel.

    Args:
        sentence (str): A string containing lowercase letters and spaces.

    Returns:
        dict: A dictionary with the vowel counts.
    """
    # Initialize a dictionary to store the vowel counts
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Find all vowels and count their occurrences
    for i in range(1, len(sentence)-1):
        if sentence[i] in 'aeiou':
            if sentence[i-1] not in 'aeiou' and sentence[i+1] not in 'aeiou':
                vowel_counts[sentence[i]] += 1

    return vowel_counts