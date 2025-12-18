"""
QUESTION:
Write a function named `count_divisible` that takes an integer `x` as input, calculates the total number of pairs of integers `(j, k)` where `1 ≤ j ≤ x` and `1 ≤ k ≤ x+1` such that `j` is divisible by `k`, and returns this count.
"""

def count_divisible(x):
    """
    This function calculates the total number of pairs of integers (j, k) 
    where 1 ≤ j ≤ x and 1 ≤ k ≤ x+1 such that j is divisible by k.
    
    Args:
        x (int): The input integer.

    Returns:
        int: The total count of pairs (j, k) where j is divisible by k.
    """
    total_count = 0
    for k in range(1, x + 2):
        total_count += len([j for j in range(1, x + 1) if j % k == 0])
    return total_count