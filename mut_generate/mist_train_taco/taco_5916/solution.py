"""
QUESTION:
A string is called a KEYENCE string when it can be changed to `keyence` by removing its contiguous substring (possibly empty) only once.

Given a string S consisting of lowercase English letters, determine if S is a KEYENCE string.

Constraints

* The length of S is between 7 and 100 (inclusive).
* S consists of lowercase English letters.

Input

Input is given from Standard Input in the following format:


S


Output

If S is a KEYENCE string, print `YES`; otherwise, print `NO`.

Examples

Input

keyofscience


Output

YES


Input

mpyszsbznf


Output

NO


Input

ashlfyha


Output

NO


Input

keyence


Output

YES
"""

def is_keyence_string(S: str) -> str:
    k = 'keyence'
    n = len(S) - 7
    
    for i in range(len(S) - n + 1):
        if S[:i] + S[i + n:] == k:
            return 'YES'
    
    return 'NO'