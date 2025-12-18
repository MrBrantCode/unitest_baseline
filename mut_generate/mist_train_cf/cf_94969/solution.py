"""
QUESTION:
Write a function named `find_closest_match` that takes two parameters: `original` and `match`. The function should return the word from the `original` string that has the minimum Levenshtein edit distance to the `match` string. If there are multiple words with the same minimum distance, return the one that appears first in the `original` string. If the minimum distance is greater than 2, return an empty string.
"""

def levenshtein_distance(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        dp[i][0] = i
    for j in range(len(s2) + 1):
        dp[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    return dp[-1][-1]


def find_closest_match(original, match):
    closest_match = ""
    closest_distance = float('inf')

    for word in original.split():
        distance = levenshtein_distance(word, match)
        if distance < closest_distance:
            closest_match = word
            closest_distance = distance

    if closest_distance <= 2:
        return closest_match
    else:
        return ""