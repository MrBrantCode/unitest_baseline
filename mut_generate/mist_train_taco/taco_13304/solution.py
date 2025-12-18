"""
QUESTION:
You are given a string S.

Takahashi can insert the character `A` at any position in this string any number of times.

Can he change S into `AKIHABARA`?

Constraints

* 1 \leq |S| \leq 50
* S consists of uppercase English letters.

Input

Input is given from Standard Input in the following format:


S


Output

If it is possible to change S into `AKIHABARA`, print `YES`; otherwise, print `NO`.

Examples

Input

KIHBR


Output

YES


Input

AKIBAHARA


Output

NO


Input

AAKIAHBAARA


Output

NO
"""

def can_form_akihabara(s: str) -> str:
    target = "AKIHABARA"
    pattern = re.compile(r'^A?KIHA?BA?RA?$')
    
    if pattern.match(s):
        return "YES"
    else:
        return "NO"