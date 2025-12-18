"""
QUESTION:
Write a function named `longest_common_subsequence` that takes two strings `str1` and `str2` as input and returns a tuple containing the length and the longest common subsequence. The function should use dynamic programming to find the longest common subsequence. The input strings will only contain uppercase English letters.
"""

def longest_common_subsequence(str1: str, str2: str):
    len1 = len(str1)
    len2 = len(str2)
    
    # Declare a 2-D DP array        
    dp = [[0]*(len2+1) for i in range(len1+1)]
    
    # Build dp[] dynamically in bottom up manner
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # store the length of longest common subsequence
    len_lcs = dp[len1][len2]

    lcs = [""] * (len_lcs+1)
    lcs[len_lcs] = ""

    # Start from the right-most-bottom-most corner and one by one store characters in lcs[]
    i = len1
    j = len2
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs[len_lcs-1] = str1[i-1]
            i-=1
            j-=1
            len_lcs-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
    return (dp[-1][-1],''.join(lcs))