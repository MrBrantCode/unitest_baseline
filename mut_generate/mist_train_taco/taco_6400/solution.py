"""
QUESTION:
The translation from the Berland language into the Birland language is not an easy task. Those languages are very similar: a berlandish word differs from a birlandish word with the same meaning a little: it is spelled (and pronounced) reversely. For example, a Berlandish word code corresponds to a Birlandish word edoc. However, it's easy to make a mistake during the «translation». Vasya translated word s from Berlandish into Birlandish as t. Help him: find out if he translated the word correctly.

Input

The first line contains word s, the second line contains word t. The words consist of lowercase Latin letters. The input data do not consist unnecessary spaces. The words are not empty and their lengths do not exceed 100 symbols.

Output

If the word t is a word s, written reversely, print YES, otherwise print NO.

Examples

Input

code
edoc


Output

YES


Input

abb
aba


Output

NO


Input

code
code


Output

NO
"""

def is_correct_translation(s: str, t: str) -> str:
    """
    Determines if the word t is the reverse of the word s.

    Parameters:
    s (str): The Berlandish word.
    t (str): The Birlandish word.

    Returns:
    str: "YES" if t is the reverse of s, otherwise "NO".
    """
    return "YES" if s == t[::-1] else "NO"