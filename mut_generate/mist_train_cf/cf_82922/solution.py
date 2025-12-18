"""
QUESTION:
Implement the `bottom_up_cut_rod` function, which takes as input an array `p` of length `n+1` and an integer `n` representing the length of a rod, where `n >= 1` and `0 <= p[i] <= 1000` for all `i`. The function should return a tuple containing the maximum possible revenue and the lengths of the pieces that make up the optimal solution. The array `p` specifies the price of a rod of length `i` for `i = 0, 1, ..., n`.
"""

def bottom_up_cut_rod(p, n):
    """
    Returns a tuple containing the maximum possible revenue and the lengths of the pieces 
    that make up the optimal solution for a rod of length n and price array p.

    Args:
    p (list): A list of length n+1 representing the prices of rods of different lengths.
    n (int): The length of the rod.

    Returns:
    tuple: A tuple containing the maximum revenue and the lengths of the pieces.
    """
    r = [0 for _ in range(n + 1)]
    s = [0 for _ in range(n + 1)]
    for j in range(1, n + 1):
        q = -1
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    cut_sizes = []
    while n > 0:
        cut_sizes.append(s[n])
        n = n - s[n]
    return r[-1], cut_sizes