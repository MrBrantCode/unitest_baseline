"""
QUESTION:
Take debugging to a whole new level:

Given a string, remove every *single* bug.

This means you must remove all instances of the word 'bug' from within a given string, *unless* the word is plural ('bugs').

For example, given 'obugobugobuoobugsoo', you should return 'ooobuoobugsoo'.

Another example: given 'obbugugo', you should return 'obugo'.

Note that all characters will be lowercase.

Happy squishing!
"""

import re

def remove_single_bugs(s: str) -> str:
    """
    Removes all instances of the word 'bug' from the given string, unless the word is plural ('bugs').

    Parameters:
    s (str): The input string from which to remove single instances of 'bug'.

    Returns:
    str: The modified string with all single instances of 'bug' removed.
    """
    return re.sub('bug(?!s)', '', s)