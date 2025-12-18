"""
QUESTION:
Write a function `gIndex(citations)` that calculates the researcher's g-index given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `ith` paper. The g-index is the highest number `g` such that the top `g` papers have together received at least `g^2` citations.

Constraints:
- `1 <= n <= 5000` where `n` is the length of `citations`
- `0 <= citations[i] <= 1000`
"""

def gIndex(citations):
    citations.sort(reverse=True)
    idx = 0
    while idx < len(citations) and citations[idx] >= idx + 1:
        idx += 1
    return idx