"""
QUESTION:
Capitalization is writing a word with its first letter as a capital letter. Your task is to capitalize the given word.

Note, that during capitalization all the letters except the first one remains unchanged.


-----Input-----

A single line contains a non-empty word. This word consists of lowercase and uppercase English letters. The length of the word will not exceed 10^3.


-----Output-----

Output the given word after capitalization.


-----Examples-----
Input
ApPLe

Output
ApPLe

Input
konjac

Output
Konjac
"""

def capitalize_word(word: str) -> str:
    """
    Capitalizes the first letter of the given word and returns the capitalized word.

    Parameters:
    word (str): The word to be capitalized.

    Returns:
    str: The capitalized word.
    """
    if not word:
        return word
    return word[0].upper() + word[1:]