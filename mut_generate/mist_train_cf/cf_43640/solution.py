"""
QUESTION:
Function `S(N)`: Given an integer `N`, calculate the sum of `(x_i + y_i)` for all losing configurations `(x_i, y_i)`, where `0 < x_i < y_i <= N`, modulo `7^10`.
"""

def S(N):
    """
    Calculate the sum of (x_i + y_i) for all losing configurations (x_i, y_i), 
    where 0 < x_i < y_i <= N, modulo 7^10.

    Args:
    N (int): The input number.

    Returns:
    int: The sum modulo 7^10.
    """
    mod = 7 ** 10
    M = N
    N = M // 30
    res = 0
    for i in range(1, 31):
        if pow(2, i, 10) == 1 or pow(2, i, 10) == 6:
            res += (3 * i * N + 3 * N * (N + 1) / 2) % mod
        else:
            res += (3 * N * (N + 1) // 2 * i + 2 * N) % mod
    return int(res % mod)