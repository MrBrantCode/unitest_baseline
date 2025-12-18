"""
QUESTION:
Write a function `min_edit_distance(str1, str2)` that calculates the minimum cost of editing two strings to make them equal. The function should consider the following constraints:

- The edit operations are insertion (cost: 1 unit), deletion (cost: 2 units), and substitution (cost: 3 units).
- The edit operations can only be performed on the characters A, B, and C.
- The input strings may contain erroneous characters that need to be removed before calculating the minimum cost.

The function should return the minimum cost of editing `str1` to `str2`.
"""

def min_edit_distance(str1, str2):
    """
    Calculate the minimum cost of editing two strings to make them equal.
    
    The edit operations are insertion (cost: 1 unit), deletion (cost: 2 units), 
    and substitution (cost: 3 units). The edit operations can only be performed 
    on the characters A, B, and C. The input strings may contain erroneous 
    characters that need to be removed before calculating the minimum cost.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    int: The minimum cost of editing str1 to str2.
    """

    # Remove any non-accepted characters
    accepted_chars = {'A', 'B', 'C'}
    str1 = ''.join([char for char in str1 if char in accepted_chars])
    str2 = ''.join([char for char in str2 if char in accepted_chars])

    m, n = len(str1), len(str2)

    # Each edit operation has a different cost
    insert_cost, delete_cost, substitute_cost = 1, 2, 3

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j * insert_cost
            elif j == 0:
                dp[i][j] = i * delete_cost
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1] + insert_cost, dp[i - 1][j] + delete_cost, dp[i - 1][j - 1] + substitute_cost)

    return dp[m][n]