"""
QUESTION:
Write a function `longest_common_subseq(s1, s2)` that takes two distinct text strings `s1` and `s2` as input and returns the length of their longest common subsequences (LCS). The function should also be able to return all common subsequences if multiple LCS of the same length exist. The complexity of the function should be optimized to at least O(n*m), where n and m are the lengths of the given strings.
"""

def longest_common_subseq(s1, s2):
    n, m = len(s1), len(s2)
    lookup = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                lookup[i][j] = lookup[i - 1][j - 1] + 1
            else:
                lookup[i][j] = max(lookup[i - 1][j], lookup[i][j - 1])
    
    i, j = n, m
    common_subseq = []
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            common_subseq.append(s1[i-1])
            i -= 1
            j -= 1
        elif lookup[i-1][j] > lookup[i][j-1]:
            i -= 1
        else:
            j -= 1
    return len(common_subseq), ''.join(reversed(common_subseq))