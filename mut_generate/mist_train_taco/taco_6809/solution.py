"""
QUESTION:
You are given strings s and t. Find one longest string that is a subsequence of both s and t.

Constraints

* s and t are strings consisting of lowercase English letters.
* 1 \leq |s|, |t| \leq 3000

Input

Input is given from Standard Input in the following format:


s
t


Output

Print one longest string that is a subsequence of both s and t. If there are multiple such strings, any of them will be accepted.

Examples

Input

axyb
abyxb


Output

axb


Input

aa
xayaz


Output

aa


Input

a
z


Output




Input

abracadabra
avadakedavra


Output

aaadara
"""

def longest_common_subsequence(s: str, t: str) -> str:
    # Initialize the DP table
    dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
    
    # Fill the DP table
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Reconstruct the longest common subsequence
    lcs = ''
    i, j = len(s), len(t)
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            lcs += s[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # The LCS is constructed in reverse order, so reverse it back
    return lcs[::-1]