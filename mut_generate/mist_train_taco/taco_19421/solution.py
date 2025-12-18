"""
QUESTION:
You are given two string S and T. Find the maximal length of some prefix of the string S which occurs in strings T as subsequence.

Input
The first line contains string S.
The second line contains string T.
Both strings consist of lowecase Latin letters.

Output
Output one integer - answer to the question.

Constraints
1 ≤ length of S, T ≤ 10^6

SAMPLE INPUT
digger
biggerdiagram

SAMPLE OUTPUT
3
"""

def maximal_prefix_subsequence_length(S: str, T: str) -> int:
    count = 0
    n = 0
    for i in S:
        for j in range(n, len(T)):
            if T[j] == i:
                count += 1
                n = j + 1
                break
        else:
            break
    return count