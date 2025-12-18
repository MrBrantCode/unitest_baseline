"""
QUESTION:
Implement the `closest_correct_word` function, which takes a misspelled word (a string) and a list of correct words (a list of strings) as input, and returns the closest correct word from the list based on the Levenshtein distance. The Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other. If there are multiple correct words with the same minimum distance, return the one that appears first in the list.
"""

def levenshtein_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

def closest_correct_word(misspelled_word, correct_words):
    min_distance = float('inf')
    closest_word = None

    for word in correct_words:
        distance = levenshtein_distance(misspelled_word, word)
        if distance < min_distance:
            min_distance = distance
            closest_word = word

    return closest_word