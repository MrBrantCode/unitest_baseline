"""
QUESTION:
If　`a = 1, b = 2, c = 3 ... z = 26`

Then `l + o + v + e = 54`

and `f + r + i + e + n + d + s + h + i + p = 108`

So `friendship` is twice stronger than `love` :-)

The input will always be in lowercase and never be empty.
"""

def calculate_word_strength(word: str) -> int:
    """
    Calculate the strength of a word based on the sum of the positions of its letters in the alphabet.

    Args:
        word (str): The input word in lowercase.

    Returns:
        int: The calculated strength of the word.
    """
    return sum((ord(c) - 96 for c in word))