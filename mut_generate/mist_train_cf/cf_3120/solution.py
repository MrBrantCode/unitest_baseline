"""
QUESTION:
Implement a function `closest_match(string, possible_matches)` that finds the closest match in a given string using the Levenshtein edit distance. If there are multiple closest matches, return the one that appears first in the original string. If there are no matches with an edit distance of 2, return an empty string. The function should take two parameters: `string` (the original string) and `possible_matches` (a list of possible match strings). The Levenshtein edit distance is the minimum number of single-character edits (insertion, deletion, or substitution) required to change one word into another.
"""

def closest_match(string, possible_matches):
    def levenshtein_distance(s1, s2):
        m = len(s1)
        n = len(s2)
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
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        
        return dp[m][n]
    
    min_distance = float('inf')
    closest_match = ""
    
    for match in possible_matches:
        distance = levenshtein_distance(string, match)
        
        if distance == 2:
            return match
        
        if distance < min_distance:
            min_distance = distance
            closest_match = match
    
    if min_distance == float('inf'):
        return ""
    
    return closest_match