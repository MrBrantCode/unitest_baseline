"""
QUESTION:
Write a function `closest_string(target, strings)` that finds the closest string to the `target` string from a list of `strings`. The closest string is defined as the string that requires the minimum number of character modifications (insertions, deletions, or substitutions) to transform it into the `target` string. If there are multiple closest strings, return the lexicographically smallest one. Assume the length of the `target` string will be at most 1000 characters, and the length of each string in the `strings` list will be at most 100 characters. The number of strings in the `strings` list will be at most 10^5.
"""

def closest_string(target, strings):
    def count_modifications(s1, s2):
        # Count the number of modifications needed to transform s2 into s1
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    
        return dp[m][n]

    closest = None
    min_modifications = float('inf')
    
    for s in strings:
        modifications = count_modifications(target, s)
        
        if modifications < min_modifications:
            closest = s
            min_modifications = modifications
        elif modifications == min_modifications and s < closest:
            closest = s
    
    return closest