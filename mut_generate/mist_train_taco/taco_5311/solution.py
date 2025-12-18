"""
QUESTION:
This contest is `CODEFESTIVAL`, which can be shortened to the string `CF` by deleting some characters.

Mr. Takahashi, full of curiosity, wondered if he could obtain `CF` from other strings in the same way.

You are given a string s consisting of uppercase English letters. Determine whether the string `CF` can be obtained from the string s by deleting some characters.

Constraints

* 2 ≤ |s| ≤ 100
* All characters in s are uppercase English letters (`A`-`Z`).

Input

The input is given from Standard Input in the following format:


s


Output

Print `Yes` if the string `CF` can be obtained from the string s by deleting some characters. Otherwise print `No`.

Examples

Input

CODEFESTIVAL


Output

Yes


Input

FESTIVALCODE


Output

No


Input

CF


Output

Yes


Input

FCF


Output

Yes
"""

import re

def can_form_cf(s: str) -> str:
    """
    Determines if the string "CF" can be obtained from the given string `s` by deleting some characters.

    Parameters:
    s (str): The input string consisting of uppercase English letters.

    Returns:
    str: "Yes" if "CF" can be formed, otherwise "No".
    """
    return 'Yes' if re.match('.*C.*F.*', s) else 'No'