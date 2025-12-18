"""
QUESTION:
You are given a string S consisting of lowercase English letters. Another string T is initially empty. Determine whether it is possible to obtain S = T by performing the following operation an arbitrary number of times:

* Append one of the following at the end of T: `dream`, `dreamer`, `erase` and `eraser`.

Constraints

* 1≦|S|≦10^5
* S consists of lowercase English letters.

Input

The input is given from Standard Input in the following format:


S


Output

If it is possible to obtain S = T, print `YES`. Otherwise, print `NO`.

Examples

Input

erasedream


Output

YES


Input

dreameraser


Output

YES


Input

dreamerer


Output

NO
"""

import re

def can_form_string(S: str) -> str:
    """
    Determines whether the string S can be formed by concatenating the substrings
    'dream', 'dreamer', 'erase', and 'eraser' in any order.

    Parameters:
    S (str): The input string consisting of lowercase English letters.

    Returns:
    str: "YES" if S can be formed using the substrings, otherwise "NO".
    """
    return 'YES' if re.match('^(dream|dreamer|erase|eraser)+$', S) else 'NO'