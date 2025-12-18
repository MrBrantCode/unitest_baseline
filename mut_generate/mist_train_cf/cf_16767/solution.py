"""
QUESTION:
Write a function `damerau_levenshtein_distance` to compute the Damerau-Levenshtein distance between two provided words. The function should take two parameters, `word1` and `word2`, both of type string. The function should return the Damerau-Levenshtein distance between `word1` and `word2`. The Damerau-Levenshtein distance is a measure of the minimum number of single-character edits (insertions, deletions or substitutions) required to change one word into the other, with the additional possibility of transpositions.
"""

def damerau_levenshtein_distance(word1, word2):
    """
    Compute the Damerau-Levenshtein distance between two words.

    The Damerau-Levenshtein distance is a measure of the minimum number of single-character edits (insertions, deletions or substitutions)
    required to change one word into the other, with the additional possibility of transpositions.

    Args:
        word1 (str): The first word.
        word2 (str): The second word.

    Returns:
        int: The Damerau-Levenshtein distance between word1 and word2.
    """

    len1 = len(word1) + 1
    len2 = len(word2) + 1

    # Matrix to store the Levenshtein distances between substrings of word1 and word2
    dp = [[0 for _ in range(len2)] for _ in range(len1)]

    # Initialize the first row and column
    for i in range(len1):
        dp[i][0] = i
    for j in range(len2):
        dp[0][j] = j

    # Fill in the rest of the matrix
    for i in range(1, len1):
        for j in range(1, len2):
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,      # Deletion
                           dp[i][j - 1] + 1,      # Insertion
                           dp[i - 1][j - 1] + cost)  # Substitution or no operation

            # If the current characters in word1 and word2 are different and the last two characters in the current substrings are the same,
            # we also consider transposition
            if i > 1 and j > 1 and word1[i - 1] == word2[j - 2] and word1[i - 2] == word2[j - 1]:
                dp[i][j] = min(dp[i][j], dp[i - 2][j - 2] + cost)

    return dp[len1 - 1][len2 - 1]