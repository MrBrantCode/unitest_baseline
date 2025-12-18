"""
QUESTION:
Given a string `S` consisting of lowercase English alphabets, write a function `partitionLabels(S)` that divides the string into the maximum number of segments such that each alphabet appears in only one segment. Return a list of integers, each representing the length of the corresponding segment. The length of `S` will be within the range `[1, 500]` and `S` will only contain lowercase English alphabets (`'a'` to `'z'`).
"""

def partitionLabels(S):
    last = {c: i for i, c in enumerate(S)}
    j = anchor = 0
    ans = []
    for i, c in enumerate(S):
        j = max(j, last[c])
        if i == j:
            ans.append(i - anchor + 1)
            anchor = i + 1
    return ans