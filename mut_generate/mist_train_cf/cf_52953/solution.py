"""
QUESTION:
Develop a function called `find_vowel_word` that takes an array of strings as input. The function should return the first word in the array that contains all five vowel characters (a, e, i, o, u) regardless of case. If no such word exists, the function should return an empty string.
"""

def find_vowel_word(words):
    """
    Returns the first word in the array that contains all five vowel characters (a, e, i, o, u) regardless of case.
    If no such word exists, returns an empty string.

    Args:
        words (list): A list of strings.

    Returns:
        str: The first word with all vowels, or an empty string if not found.
    """

    vowels = set("aeiou")
    for word in words:
        if set(word.lower()).issuperset(vowels):
            return word
    return ""