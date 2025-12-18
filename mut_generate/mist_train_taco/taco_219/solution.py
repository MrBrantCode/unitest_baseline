"""
QUESTION:
Taro had his own personal computer and set a password for login. However, Taro inadvertently forgot the password. Then, remembering that there was a piece of paper with the password written down, Taro found the paper and was surprised to see it. The paper was cut and there were only fragments, and there were some stains that made it unreadable. Taro decided to guess the password by referring to the memo.

Constraints

* The length of the character strings A and B is 1 to 1000 characters.
* The length of the B string does not exceed the length of the A string.

Input

String A
String B

Output

Output "Yes" or "No" on one line.

Examples

Input

ABCDE
ABC


Output

Yes


Input

KUSATSU
KSATSU


Output

No


Input

ABCABC
ACBA_B


Output

No


Input

RUPCUAPC
__PC


Output

Yes


Input

AIZU
_A


Output

No
"""

def is_password_guess_correct(A: str, B: str) -> str:
    length_a = len(A)
    length_b = len(B)
    
    for i in range(length_a - length_b + 1):
        for j in range(length_b):
            if B[j] == '_' or A[i + j] == B[j]:
                continue
            else:
                break
        else:
            return 'Yes'
    return 'No'