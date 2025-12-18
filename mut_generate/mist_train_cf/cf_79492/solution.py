"""
QUESTION:
Write a function called `levenshtein_distance(str1, str2)` that calculates the minimum number of single character alterations (insertions, deletions, or replacements) required to transform string `str1` into string `str2`. The function should return this minimum number.
"""

def levenshtein_distance(str1, str2):
    m, n = len(str1), len(str2)
    d = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(m+1):
        d[i][0] = i
    for j in range(n+1):
        d[0][j] = j
        
    for j in range(1, n+1):
        for i in range(1, m+1):
            if str1[i-1] == str2[j-1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            d[i][j] = min(d[i-1][j] + 1,                      # deletion
                          d[i][j-1] + 1,                      # insertion
                          d[i-1][j-1] + substitution_cost)   # substitution
    return d[m][n]