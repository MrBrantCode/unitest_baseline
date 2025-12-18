"""
QUESTION:
Calculate the result of the expression `(1900 * M + 100 * (N - M)) * (2 ** M)` where N and M are integers. Implement a function `calculate_result(N, M)` that takes two integers `N` and `M` as input and returns the calculated result, given that `1 ≤ M ≤ N ≤ 10^9`.
"""

def calculate_result(N, M):
    """
    Calculate the result of the expression `(1900 * M + 100 * (N - M)) * (2 ** M)`

    Args:
        N (int): An integer where 1 ≤ M ≤ N ≤ 10^9
        M (int): An integer where 1 ≤ M ≤ N ≤ 10^9

    Returns:
        int: The calculated result
    """
    return (1900 * M + 100 * (N - M)) * (2 ** M)