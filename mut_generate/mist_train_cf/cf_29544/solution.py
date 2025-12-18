"""
QUESTION:
Implement a function `longest_common_subsequence_lengths(query_nsubsequences, query_subsequences)` that calculates the length of the longest common subsequence between each given subsequence and all other subsequences in the list. 

The function takes two parameters: `query_nsubsequences` (the number of subsequences) and `query_subsequences` (a list of strings representing the subsequences). 

The function should return a list of integers representing the length of the longest common subsequence between each given subsequence and all other subsequences in the list.

Restrictions: The length of each subsequence will not exceed 1000 characters, and the number of subsequences will not exceed 1000.
"""

def longest_common_subsequence_lengths(query_nsubsequences, query_subsequences):
    def longest_common_subsequence_length(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

    result = []
    for i in range(query_nsubsequences):
        sub_seq = query_subsequences[i]
        max_length = 0
        for j in range(query_nsubsequences):
            if i != j:
                max_length = max(max_length, longest_common_subsequence_length(sub_seq, query_subsequences[j]))
        result.append(max_length)
    return result