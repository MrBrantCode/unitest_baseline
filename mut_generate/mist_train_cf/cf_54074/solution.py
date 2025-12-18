"""
QUESTION:
Write a function `get_closest_vowel(word)` that finds the closest vowel to the end of the input word, where the vowel is positioned between two consonants. The function should be case sensitive and should not consider vowels at the beginning or end of the word. If no such vowel exists, the function should return an empty string. The input string is assumed to be formed exclusively by English letters.
"""

def get_closest_vowel(word):
    """
    Accepts a single word input, then ascertains the closest vowel positioned between 
    two consonants originating from the word's right-most character, accounting for 
    case sensitivity. Vowels at the beginning or end of the word should not be 
    considered, and an empty string should be returned if the specified vowel does not 
    exist. The input string is assumed to be formed exclusively by English letters.
    """

    # reverse the word to start from the right-most character
    reversed_word = word[::-1]

    for i in range(1, len(reversed_word)-1):
        # check if current character is a vowel, the previous and next characters are consonants
        if reversed_word[i] in 'aeiouAEIOU' and reversed_word[i-1] not in 'aeiouAEIOU' and reversed_word[i+1] not in 'aeiouAEIOU':
            return reversed_word[i]  # found the vowel

    return ""  # return empty string if no such vowel exists