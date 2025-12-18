"""
QUESTION:
Create a function named `closest_string` that takes in two parameters: 
- A string `string` (1 <= len(string) <= 1000): The given string.
- A list of strings `strings` (1 <= len(strings) <= 10^5): The list of strings to compare. The length of each string in the list will be at most 100 characters.

The function should return a string, which is the closest string to the given string. The closest string is defined as the string that requires the minimum number of character modifications (insertions, deletions, or substitutions) to transform it into the given string. If there are multiple closest strings, return the lexicographically smallest one.
"""

def closest_string(string, strings):
    def levenshtein_distance(s1, s2):
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i

        for j in range(n+1):
            dp[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

        return dp[m][n]

    closest = strings[0]
    closest_modifications = float('inf')

    for s in strings:
        modifications = levenshtein_distance(string, s)
        if modifications < closest_modifications:
            closest = s
            closest_modifications = modifications
        elif modifications == closest_modifications:
            closest = min(closest, s)

    return closest