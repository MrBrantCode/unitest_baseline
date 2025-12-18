"""
QUESTION:
Write a function called `getFarthestVowel` that takes a string of English letters as input and returns the farthest vowel that stands between two consonants from the left side of the word. Vowels at the beginning and end of the word do not count. If no such vowel is found, return an empty string. The function should be case sensitive.
"""

def getFarthestVowel(word):
    """
    This function finds the farthest vowel that stands between two consonants 
    from the left side of the word. Vowels at the beginning and end of the 
    word do not count. If no such vowel is found, return an empty string. 
    The function is case sensitive.

    Args:
        word (str): A string of English letters.

    Returns:
        str: The farthest vowel that stands between two consonants, or an empty string if not found.
    """

    farthest_vowel = ""
    vowels = set('aeiouAEIOU')
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            farthest_vowel = word[i]
    return farthest_vowel