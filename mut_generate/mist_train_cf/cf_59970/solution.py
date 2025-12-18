"""
QUESTION:
Given a string S and a pattern string P, write a function named patternMatch(S, P) that returns a tuple with three values: the last occurrence of pattern P, its index, and the count of occurrences. The function should handle case insensitivity, pattern P with multiple characters, and situations where pattern P doesn't exist in S.
"""

def patternMatch(S, P):
    S = S.lower()
    P = P.lower()
    Position = S.rfind(P)
    if Position == -1:
        return (None, None, 0)
    Count = S.count(P)
    return (P, Position, Count)