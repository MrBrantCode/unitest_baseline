"""
QUESTION:
Define a function F(n) that calculates the count of distinct terms √(x+√y+√z), where x, y, and z are positive integers, y and z are not perfect squares, and x ≤ n, that can be denested into the sum and/or difference of a finite number of square roots. Implement this function to calculate F(5000000). The function should only consider distinct denestable roots, i.e., nested roots with identical values are considered the same.
"""

def entrance(n):
    """
    Calculate the count of distinct terms √(x+√y+√z) that can be denested into the sum and/or difference of a finite number of square roots.
    
    Parameters:
    n (int): The upper limit for x.
    
    Returns:
    int: The count of distinct denestable terms.
    """
    done = [False] * (n + 1)
    denest = [(1, 1, 1), (2, 2, 3), (3, 2, 2), (5, 2, 3), (6, 1, 6), (6, 3, 8), (7, 6, 12), (8, 3, 5), (8, 15, 15), (11, 22, 45), (13, 10, 28), (14, 5, 7), (20, 12, 96), (22, 6, 34), (24, 5, 6), (24, 7, 21), (28, 11, 57), (48, 23, 120), (97, 36, 280)]

    for d in denest:
        (x, y, z) = d
        while x <= n:
            done[x] = True
            x += z + 1
            y += 1
            z += (y << 1)

    return done[1:n + 1].count(True)