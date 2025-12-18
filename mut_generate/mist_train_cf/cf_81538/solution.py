"""
QUESTION:
Given a string `S` composed solely of lowercase letters and an integer `K`, write a function `orderlyQueue(S, K)` that determines the lexicographically smallest string that can be obtained after performing an arbitrary number of moves, where each move selects one of the first `K` letters (counting from the left), removes it, and appends it to the end of the string. The function should satisfy the constraints: `1 <= K <= S.length <= 1000`.
"""

def orderlyQueue(S, K):
    if K == 1:
        return min(S[i:] + S[:i] for i in range(len(S)))
    return "".join(sorted(S))