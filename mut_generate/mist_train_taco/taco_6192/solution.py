"""
QUESTION:
Ringo is giving a present to Snuke.

Ringo has found out that Snuke loves yakiniku (a Japanese term meaning grilled meat. yaki: grilled, niku: meat). He supposes that Snuke likes grilled things starting with `YAKI` in Japanese, and does not like other things.

You are given a string S representing the Japanese name of Ringo's present to Snuke. Determine whether S starts with `YAKI`.

Constraints

* 1 \leq |S| \leq 10
* S consists of uppercase English letters.

Input

Input is given from Standard Input in the following format:


S


Output

If S starts with `YAKI`, print `Yes`; otherwise, print `No`.

Examples

Input

YAKINIKU


Output

Yes


Input

TAKOYAKI


Output

No


Input

YAK


Output

No
"""

def starts_with_yaki(s: str) -> str:
    """
    Determines whether the given string starts with 'YAKI'.

    Parameters:
    s (str): The input string to check.

    Returns:
    str: 'Yes' if the string starts with 'YAKI', otherwise 'No'.
    """
    if s.startswith('YAKI'):
        return 'Yes'
    else:
        return 'No'