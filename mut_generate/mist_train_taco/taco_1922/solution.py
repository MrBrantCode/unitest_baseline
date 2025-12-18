"""
QUESTION:
Snuke built an online judge to hold a programming contest.

When a program is submitted to the judge, the judge returns a verdict, which is a two-character string that appears in the string S as a contiguous substring. (The judge can return any two-character substring of S.)

Determine whether the judge can return the string `AC` as the verdict to a program.

Constraints

* 2 \leq |S| \leq 5
* S consists of uppercase English letters.

Input

Input is given from Standard Input in the following format:


S


Output

If the judge can return the string `AC` as a verdict to a program, print `Yes`; if it cannot, print `No`.

Examples

Input

BACD


Output

Yes


Input

ABCD


Output

No


Input

CABD


Output

No


Input

ACACA


Output

Yes


Input

XX


Output

No
"""

def can_return_ac_verdict(S: str) -> str:
    for s, ns in zip(S, S[1:]):
        if s + ns == 'AC':
            return 'Yes'
    return 'No'