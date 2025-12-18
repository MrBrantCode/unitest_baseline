"""
QUESTION:
Write a function `append_char` that takes a string `s` and a character `c` as inputs. The function should append the character `c` at the start and end of the string `s` if `c` is a vowel. If `c` is not a vowel, it should append the character following `c` in the English alphabet. If `c` is "z" or "Z", it should be replaced with "a" or "A" respectively.
"""

def append_char(s, c):
    """
    Appends a character c at the start and end of the string s if c is a vowel.
    If c is not a vowel, it appends the character following c in the English alphabet.
    If c is "z" or "Z", it is replaced with "a" or "A" respectively.

    Args:
        s (str): The input string.
        c (str): The input character.

    Returns:
        str: The modified string with the character appended at the start and end.
    """

    vowels = 'aeiouAEIOU'
    if c in vowels:
        return c + s + c
    else:
        if c == 'z':
            c = 'a'
        elif c == 'Z':
            c = 'A'
        else:
            c = chr(ord(c) + 1)
        return c + s + c