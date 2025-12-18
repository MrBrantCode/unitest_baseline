"""
QUESTION:
You are given a string S of length 2 or 3 consisting of lowercase English letters. If the length of the string is 2, print it as is; if the length is 3, print the string after reversing it.

Constraints

* The length of S is 2 or 3.
* S consists of lowercase English letters.

Input

Input is given from Standard Input in the following format:


S


Output

If the length of S is 2, print S as is; if the length is 3, print S after reversing it.

Examples

Input

abc


Output

cba


Input

ac


Output

ac
"""

def process_string(S: str) -> str:
    if len(S) == 2:
        return S
    elif len(S) == 3:
        return S[::-1]