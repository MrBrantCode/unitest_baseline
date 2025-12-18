"""
QUESTION:
Unscramble the eggs.

The string given to your function has had an "egg" inserted directly after each consonant.  You need to return the string before it became eggcoded.

## Example

Kata is supposed to be for beginners to practice regular expressions, so commenting would be appreciated.
"""

def unscramble_eggs(word):
    """
    Unscrambles the given word by removing the "egg" inserted after each consonant.

    Parameters:
    word (str): The scrambled word with "egg" inserted after each consonant.

    Returns:
    str: The original word before it was scrambled.
    """
    return word.replace('egg', '')