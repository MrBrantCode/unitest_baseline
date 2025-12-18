"""
QUESTION:
Write a function `concatenate_and_analyze` that takes two strings as input, concatenates them using the `reduce` function from the `functools` module, reverses the resulting string, and returns the reversed string along with the count of vowels and consonants. The function should consider both lowercase and uppercase vowels and treat non-alphabetic characters as neither vowels nor consonants.
"""

import functools

def concatenate_and_analyze(str1, str2):
    """
    Concatenates two strings, reverses the result, and returns the reversed string 
    along with the count of vowels and consonants.

    Parameters:
    str1 (str): The first string.
    str2 (str): The second string.

    Returns:
    tuple: A tuple containing the reversed concatenated string, the count of vowels, 
    and the count of consonants.
    """
    # Using reduce function for string concatenation
    concatenated_str = functools.reduce(lambda x, y: x + y, [str1, str2])
    reverse_str = concatenated_str[::-1]
    
    # Count the vowels and consonants
    vowels = 'aeiou'
    vowels = vowels + vowels.upper()
    vowels_count = 0
    consonants_count = 0

    for i in reverse_str:
        if i in vowels:
            vowels_count += 1
        elif i.isalpha():
            consonants_count += 1

    return reverse_str, vowels_count, consonants_count