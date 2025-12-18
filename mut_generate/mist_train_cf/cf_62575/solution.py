"""
QUESTION:
Create a function `vowel_consonant_ratio(word)` that calculates the ratio of vowels to consonants in a given word. The function should consider both uppercase and lowercase letters. In the English language, 'y' is considered a consonant. If the word contains no consonants, the function should return a message stating that the ratio cannot be computed.
"""

def vowel_consonant_ratio(word):
    """
    Calculate the ratio of vowels to consonants in a given word.

    Args:
        word (str): The input word.

    Returns:
        float or str: The ratio of vowels to consonants if the word contains consonants, otherwise a message stating that the ratio cannot be computed.
    """
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

    vowel_count = len([char for char in word if char in vowels])
    consonant_count = len([char for char in word if char in consonants])

    if consonant_count == 0:
        return "No consonants in the word, cannot compute a ratio"

    return vowel_count / consonant_count