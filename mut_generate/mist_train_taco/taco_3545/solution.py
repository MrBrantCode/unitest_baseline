"""
QUESTION:
You are given a string S. Find the number of different substrings in S.

Input
One line containing a string S consisting of lowercase Latin letters.

Output
Output one integer - answer to the question.

Constraints
1 ≤ length of S ≤ 1200

SAMPLE INPUT
abc

SAMPLE OUTPUT
6
"""

def count_unique_substrings(s: str) -> int:
    dt = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring not in dt:
                dt[substring] = 1
    return len(dt)