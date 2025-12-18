"""
QUESTION:
Write a function `levenshtein_distance(s: str, t: str) -> int` to calculate the minimum number of single-character operations (insertions, deletions, or substitutions) required to change string `s` into string `t`. The function should be able to handle strings with Unicode characters. The function should return an integer representing the Levenshtein distance between the two input strings. 

The function should also include error handling to ensure that both `s` and `t` are strings before calculating the Levenshtein distance.
"""

def levenshtein_distance(s: str, t: str) -> int:
    # Input validation: ensure both inputs are strings
    if not isinstance(s, str):
        s = str(s)
    if not isinstance(t, str):
        t = str(t)
    
    # Create a table to store results of subproblems
    m, n = len(s), len(t)
    d = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the table for base case results
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    # Fill in the table
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            # cost of substitution
            subst_cost = 0 if s[i - 1] == t[j - 1] else 1
            d[i][j] = min(
                d[i - 1][j] + 1,                   # deletion
                d[i][j - 1] + 1,                   # insertion
                d[i - 1][j - 1] + subst_cost       # substitution
            )

    return d[m][n]