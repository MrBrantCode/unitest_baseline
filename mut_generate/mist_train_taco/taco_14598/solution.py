"""
QUESTION:
An integer partition of n is a weakly decreasing list of positive integers which sum to n.

For example, there are 7 integer partitions of 5:

[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].

Write a function named partitions which returns the number of integer partitions of n.  The function should be able to find the number of integer partitions of n for n as least as large as 100.
"""

def count_integer_partitions(n: int) -> int:
    """
    Returns the number of integer partitions of n.

    Parameters:
    n (int): The integer for which to find the number of partitions.

    Returns:
    int: The number of integer partitions of n.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    
    # Initialize the partition table
    c = [[1]]
    
    # Fill the partition table
    for x in range(1, n + 1):
        c.append([0])
        for m in range(1, x + 1):
            c[x].append(c[x][m - 1] + c[x - m][min(m, x - m)])
    
    return c[n][n]