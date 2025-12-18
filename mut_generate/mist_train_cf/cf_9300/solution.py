"""
QUESTION:
Create a function `concat_vowels` that takes two strings as input, `str1` and `str2`. The function should return a new string that is the concatenation of only the vowels that appear in both `str1` and `str2`. Vowels are defined as 'a', 'e', 'i', 'o', and 'u'.
"""

def concat_vowels(str1, str2):
    """
    Concatenates the vowels that appear in both input strings.

    Args:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    str: A new string containing the vowels common to both input strings.
    """
    vowels = "aeiou"
    return "".join(char for char in str1 if char in vowels and char in str2)