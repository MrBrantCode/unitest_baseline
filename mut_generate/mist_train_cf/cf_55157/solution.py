"""
QUESTION:
Write a function `expected_final_count(n)` to calculate the expected final count of black sheep `E(n)` when there are initially `n` white sheep and `n` black sheep, and a sheep is removed from the white flock every time a white sheep bleats. The function should return the result rounded to six decimal places.

The function should consider the optimal strategy of removing a white sheep immediately after it bleats to maximize the expected final count of black sheep. The function should use dynamic programming to compute the expected values based on the probabilities of the next sheep to bleat being white or black.

Note: The function should be efficient enough to handle large values of `n`.
"""

def expected_final_count(n):
    """
    Calculate the expected final count of black sheep E(n) when there are initially n white sheep and n black sheep.

    Args:
    n (int): The number of white and black sheep.

    Returns:
    float: The expected final count of black sheep rounded to six decimal places.
    """

    dp = [[0.0]*(n+1) for _ in range(n+1)]

    # Iterating from the end
    for a in range(n+1):
        for b in range(n, -1, -1):
            if a == 0: 
                dp[a][b] = b
            else:
                dp[a][b] = (a/(a+b))*dp[max(a-1, 0)][b] + (b/(a+b))*(dp[a][b-1] + 1)

    return round(dp[n][n], 6)