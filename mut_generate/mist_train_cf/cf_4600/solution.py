"""
QUESTION:
Write a function `count_vowels_and_consonants` that takes a string input from the user. The function should convert the string to uppercase, count the number of vowels (a, e, i, o, u) and consonants, and calculate the ratio of vowels to consonants. The function should return the uppercase string, vowel count, consonant count, and the vowel to consonant ratio as a decimal rounded to two decimal places.
"""

def count_vowels_and_consonants(sentence):
    """
    This function takes a string input, converts it to uppercase, counts the number of vowels and consonants, 
    and calculates the ratio of vowels to consonants.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing the uppercase string, vowel count, consonant count, and the vowel to consonant ratio.
    """
    sentence = sentence.upper()
    vowels = 0
    consonants = 0

    for char in sentence:
        if char in ['A', 'E', 'I', 'O', 'U']:
            vowels += 1
        elif char.isalpha():
            consonants += 1

    if consonants == 0:
        ratio = 0
    else:
        ratio = round(vowels / consonants, 2)

    return sentence, vowels, consonants, ratio