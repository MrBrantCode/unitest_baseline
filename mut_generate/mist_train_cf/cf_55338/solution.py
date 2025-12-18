"""
QUESTION:
Write a function `count_vowels(sentence)` that calculates the total number of vowels and the frequency of each vowel in a given sentence, considering capitalization and punctuation. The function should return two values: the total count of vowels and a dictionary with the frequency of each vowel. The function should ignore case sensitivity by treating both lowercase and uppercase vowels as the same.
"""

def count_vowels(sentence):
    """
    Calculate the total number of vowels and the frequency of each vowel in a given sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: A tuple containing the total count of vowels and a dictionary with the frequency of each vowel.
    """
    sentence = sentence.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowels = {vowel: 0 for vowel in vowels}
    total_count = 0
    for char in sentence:
        if char in vowels:
            count_vowels[char] += 1
            total_count += 1
    return total_count, count_vowels