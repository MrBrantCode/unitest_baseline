"""
QUESTION:
Write a function named `count_vowels_and_consonants` that takes a string as input and counts the occurrences of each vowel (a, e, i, o, u) and consonants in the string, considering both lowercase and uppercase letters. The function should ignore special characters and punctuation marks, and output the total count of vowels and consonants, as well as the count of each vowel. The input string may contain any characters.
"""

def count_vowels_and_consonants(string):
    """
    Counts the occurrences of each vowel (a, e, i, o, u) and consonants in the input string.

    Args:
        string (str): Input string to count vowels and consonants.

    Returns:
        tuple: A dictionary with vowel counts and the total count of consonants.
    """

    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    cleaned_string = ''.join(c for c in string if c.isalpha())

    vowel_counts = {vowel: 0 for vowel in vowels}
    consonant_count = 0

    for char in cleaned_string:
        if char in vowels:
            vowel_counts[char] += 1
        else:
            consonant_count += 1

    total_vowels = sum(vowel_counts.values())
    total_consonants = consonant_count

    return vowel_counts, total_consonants