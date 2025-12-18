"""
QUESTION:
Snuke has a string S consisting of three kinds of letters: `a`, `b` and `c`.

He has a phobia for palindromes, and wants to permute the characters in S so that S will not contain a palindrome of length 2 or more as a substring. Determine whether this is possible.

Constraints

* 1 \leq |S| \leq 10^5
* S consists of `a`, `b` and `c`.

Input

Input is given from Standard Input in the following format:


S


Output

If the objective is achievable, print `YES`; if it is unachievable, print `NO`.

Examples

Input

abac


Output

YES


Input

aba


Output

NO


Input

babacccabab


Output

YES
"""

from collections import defaultdict

def can_avoid_palindromes(s: str) -> str:
    # Count the frequency of each character
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    
    # Extract the counts of 'a', 'b', and 'c'
    a, b, c = d['a'], d['b'], d['c']
    
    # Find the maximum and minimum counts
    mx = max(a, b, c)
    mn = min(a, b, c)
    
    # Check if the difference between the maximum and minimum counts is at least 2
    if mx - mn >= 2:
        return 'NO'
    else:
        return 'YES'