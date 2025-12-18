"""
QUESTION:
Implement a function `edit_distance(s1, s2)` that calculates the minimum number of operations (insertions, deletions, and substitutions) required to transform string `s1` into string `s2`. The costs of operations are as follows: substitutions cost 2, insertions and deletions cost 1. The function should take two strings `s1` and `s2` as input and return the minimum edit distance between them.
"""

def edit_distance(s1, s2):
    len_str1 = len(s1)
    len_str2 = len(s2)

    dp = [[0 for _ in range(len_str2+1)] for _ in range(len_str1+1)]

    # Initialize the matrix 'dp' with the costs of insertions and deletions
    for i in range(len_str1+1):
        dp[i][0] = i
    for j in range(len_str2+1):
        dp[0][j] = j

    for i in range(1, len_str1+1):
        for j in range(1, len_str2+1):
            # If the characters are the same, no operation is needed
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                substitutes = dp[i-1][j-1] + 2
                deletes = dp[i-1][j] + 1
                inserts = dp[i][j-1] + 1
                
                dp[i][j] = min(substitutes, deletes, inserts)

    # The entry dp[len_str1][len_str2] is the minimized cost
    return dp[len_str1][len_str2]