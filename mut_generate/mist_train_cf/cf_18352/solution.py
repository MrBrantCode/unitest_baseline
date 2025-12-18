"""
QUESTION:
Write a function called `count_vowels` that takes a string of text as input. The function should count the number of vowels in the text, ignoring any consecutive vowels (counting them as one) and vowels immediately followed by the consonants 'v', 'x', or 'z'.
"""

def count_vowels(text):
    """
    This function counts the number of vowels in a given text, ignoring any consecutive vowels 
    and vowels immediately followed by the consonants 'v', 'x', or 'z'.

    Parameters:
    text (str): The input string.

    Returns:
    int: The count of vowels in the text.
    """
    vowels = 'aeiou'
    count = 0
    prev_vowel = False
    for char in text.lower():
        if char in vowels:
            if not prev_vowel:
                count += 1
                prev_vowel = True
            if char not in 'vzx':
                continue
            else:
                prev_vowel = False
        else:
            prev_vowel = False
    return count