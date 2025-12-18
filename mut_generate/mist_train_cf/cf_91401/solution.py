"""
QUESTION:
Write a function named `count_vowels` that takes a string `sentence` as input, counts the occurrences of each vowel (a, e, i, o, u), and excludes any vowels that are immediately preceded or followed by another vowel. Return a dictionary with vowels as keys and their counts as values.
"""

def count_vowels(sentence):
    """
    Counts the occurrences of each vowel (a, e, i, o, u) in a sentence, 
    excluding any vowels that are immediately preceded or followed by another vowel.

    Args:
        sentence (str): The input sentence.

    Returns:
        dict: A dictionary with vowels as keys and their counts as values.
    """
    vowels_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    sentence = sentence.lower()
    
    for i in range(len(sentence)):
        if sentence[i] in vowels_count:
            if (i == 0 or sentence[i-1] not in vowels_count) and (i == len(sentence)-1 or sentence[i+1] not in vowels_count):
                vowels_count[sentence[i]] += 1
                
    return vowels_count