"""
QUESTION:
Implement a function `EditSequence(str1, str2)` that takes two strings `str1` and `str2` as input and returns a tuple containing the sequence of edits (insertions, deletions, or substitutions) required to transform `str1` into `str2`, along with the Levenshtein distance (edit distance) between the two strings. The sequence of edits should include the action type, the character edited, and the count of the action. The function should be efficient and use dynamic programming to compute the edit distance and sequence of edits.
"""

def EditSequence(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    dp = [[0 for i in range(len2+1)] for j in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    i, j = len1, len2
    sequence = []
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i-1][j-1] + 1:
            sequence.append(('substitute', str1[i-1], str2[j-1], 1))
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i][j-1] + 1:
            sequence.append(('insert', str2[j-1], 1))
            j -= 1
        else:
            sequence.append(('delete', str1[i-1], 1))
            i -= 1
    while i > 0:
        sequence.append(('delete', str1[i-1], 1))
        i -= 1
    while j > 0:
        sequence.append(('insert', str2[j-1], 1))
        j -= 1
    sequence.reverse()
    return sequence, dp[len1][len2]