"""
QUESTION:
Write a function `findLCS(String1, String2)` to find the longest common subsequence between two strings `String1` and `String2`, where the subsequence must consist of alternating vowels and consonants from the two strings. If there are multiple valid subsequences of the same length, return the one with the smallest lexicographical order. Assume the input strings only contain uppercase English letters and consider 'A', 'E', 'I', 'O', 'U' as vowels.
"""

def findLCS(String1, String2):
    n1 = len(String1)
    n2 = len(String2)
    
    def isVowel(char):
        return char in ['A', 'E', 'I', 'O', 'U']

    # Create a 2D matrix to store the lengths of the LCS
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    # Fill in the matrix using dynamic programming
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            # If the characters match and have alternating vowels and consonants
            if String1[i-1] == String2[j-1] and (isVowel(String1[i-1]) != isVowel(String2[j-1])):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Construct the LCS string by backtracking from the bottom-right cell
    lcs = ""
    i = n1
    j = n2
    while i > 0 and j > 0:
        if String1[i-1] == String2[j-1] and (isVowel(String1[i-1]) != isVowel(String2[j-1])):
            lcs = String1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return lcs