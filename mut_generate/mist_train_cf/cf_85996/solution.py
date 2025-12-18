"""
QUESTION:
Write a function `minSteps` that takes two strings `word1` and `word2` as input and returns the minimum number of steps required to make `word1` and `word2` the same. In one step, you can delete exactly one character in either string or swap two characters in the same string. However, you can only delete characters that are vowels (a, e, i, o, u) and you can only swap consonants. If it is not possible to make the two strings the same using the given constraints, return -1.

The input strings `word1` and `word2` consist of only lowercase English letters and have lengths between 1 and 500, inclusive.
"""

def minSteps(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    vowels = ('a', 'e', 'i', 'o', 'u')
    consonants_word1 = [ch for ch in word1 if ch not in vowels]
    consonants_word2 = [ch for ch in word2 if ch not in vowels]
    if sorted(consonants_word1) != sorted(consonants_word2):
        return -1
    else:
        steps = m + n - 2 * dp[m][n]
        return steps