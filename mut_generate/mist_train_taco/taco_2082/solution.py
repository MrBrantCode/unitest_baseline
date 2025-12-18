"""
QUESTION:
You are given a string of words (x), for each word within the string you need to turn the word 'inside out'. By this I mean the internal letters will move out, and the external letters move toward the centre. 

If the word is even length, all letters will move. If the length is odd, you are expected to leave the 'middle' letter of the word where it is. 

An example should clarify:

'taxi' would become 'atix'
'taxis' would become 'atxsi'
"""

import re

def inside_out_string(s: str) -> str:
    """
    Transforms each word in the input string by moving the internal letters out and the external letters toward the center.

    Parameters:
    s (str): The input string containing words to be transformed.

    Returns:
    str: The transformed string where each word is "inside out".
    """
    return re.sub(r'\S+', lambda m: inside_out_word(m.group()), s)

def inside_out_word(s: str) -> str:
    """
    Transforms a single word by moving the internal letters out and the external letters toward the center.

    Parameters:
    s (str): The word to be transformed.

    Returns:
    str: The transformed word.
    """
    i, j = len(s) // 2, (len(s) + 1) // 2
    return s[:i][::-1] + s[i:j] + s[j:][::-1]