"""
QUESTION:
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except `"aeiou"`. 

We shall assign the following values: `a = 1, b = 2, c = 3, .... z = 26`.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z **~~o~~** d **~~ia~~** cs"

For C: do not mutate input.

More examples in test cases. Good luck!

If you like this Kata, please try:

[Word values](https://www.codewars.com/kata/598d91785d4ce3ec4f000018)

[Vowel-consonant lexicon](https://www.codewars.com/kata/59cf8bed1a68b75ffb000026)
"""

import re

def highest_consonant_value(s: str) -> int:
    """
    Calculate the highest value of consonant substrings in a given string.

    Parameters:
    s (str): A string containing only lowercase alphabetic characters and no spaces.

    Returns:
    int: The highest value of consonant substrings.
    """
    # Split the string by vowels to get consonant substrings
    consonant_substrings = re.split('[aeiou]+', s)
    
    # Calculate the value of each consonant substring
    consonant_values = [sum((ord(c) - 96 for c in subs)) for subs in consonant_substrings if subs]
    
    # Return the maximum value among all consonant substrings
    return max(consonant_values) if consonant_values else 0