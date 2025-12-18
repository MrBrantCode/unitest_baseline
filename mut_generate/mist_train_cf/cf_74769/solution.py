"""
QUESTION:
Write a function `find_occurrences(S, P)` that finds all occurrences of pattern `P` in string `S`, considering overlapping patterns and case sensitivity. The function should return a list of starting indices of all occurrences of `P` in `S`. If `P` is not found in `S`, return the message 'Pattern not found in text'.
"""

def find_occurrences(S, P):
    occurrences = []
    P_len = len(P)
    S_len = len(S)
    for i in range(S_len - P_len + 1):
        if S[i:i + P_len] == P:
            occurrences.append(i)
    if not occurrences:
        return 'Pattern not found in text'
    else:
        return occurrences