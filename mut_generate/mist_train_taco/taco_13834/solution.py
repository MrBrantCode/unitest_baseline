"""
QUESTION:
A Hitachi string is a concatenation of one or more copies of the string `hi`.

For example, `hi` and `hihi` are Hitachi strings, while `ha` and `hii` are not.

Given a string S, determine whether S is a Hitachi string.

Constraints

* The length of S is between 1 and 10 (inclusive).
* S is a string consisting of lowercase English letters.

Input

Input is given from Standard Input in the following format:


S


Output

If S is a Hitachi string, print `Yes`; otherwise, print `No`.

Examples

Input

hihi


Output

Yes


Input

hi


Output

Yes


Input

ha


Output

No
"""

def is_hitachi_string(S: str) -> str:
    if len(S) == S.count('hi') * 2:
        return 'Yes'
    else:
        return 'No'