"""
QUESTION:
Problem

Given the string S, which consists of lowercase letters and numbers. Follow the steps below to compress the length of string S.

1. Change the order of the characters in the character string to any order.
Example: "0ig3he12fz99"-> "efghiz012399"
2. Perform the following operations any number of times.


* Select a contiguous substring of "abcdefghijklmnopqrstuvwxyz" in the string and replace it with (first character)'-' (last character).
Example: "efghiz012399"-> "e-iz012399"
* Select a string with a tolerance of 1 (a continuous substring of "0123456789") in the string and replace it with (first digit)'-' (last digit).
Example: "e-iz012399"-> "e-iz0-399"




Find the minimum length of the string obtained by compressing the string S.

Constraints

* 1 ≤ | S | ≤ 100
* String S contains only lowercase letters and numbers

Input

The string S is given on one line.

Output

Output the minimum value of the length of the character string obtained by compressing the character string S on one line. If it cannot be compressed, output the length of the original string S.

Examples

Input

0ig3he12fz99


Output

9


Input

1122334455


Output

6
"""

from collections import defaultdict

def compress_string_length(S: str) -> int:
    S = sorted(S)
    S = list(map(ord, S))
    ans = 0
    
    while len(S) > 0:
        mn = S[0]
        S.remove(mn)
        nxt = mn + 1
        succ = 1
        
        while True:
            if nxt in S:
                S.remove(nxt)
                succ += 1
                nxt += 1
            else:
                break
        
        ans += min(3, succ)
    
    return ans