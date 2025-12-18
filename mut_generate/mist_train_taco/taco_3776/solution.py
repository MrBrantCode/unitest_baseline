"""
QUESTION:
When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

`This kata is meant for beginners. Rank and upvote to bring it out of beta`
"""

def get_alphabet_position(letter: str) -> str:
    """
    Returns the position of the given letter in the alphabet.

    Parameters:
    letter (str): A single character string representing the letter.

    Returns:
    str: A string in the format "Position of alphabet: X", where X is the position of the letter.
    """
    return 'Position of alphabet: {}'.format(ord(letter) - 96)