"""
QUESTION:
Find the number of ways to choose a pair of an even number and an odd number from the positive integers between 1 and K (inclusive). The order does not matter.

-----Constraints-----
 - 2\leq K\leq 100
 - K is an integer.

-----Input-----
Input is given from Standard Input in the following format:
K

-----Output-----
Print the number of ways to choose a pair of an even number and an odd number from the positive integers between 1 and K (inclusive).

-----Sample Input-----
3

-----Sample Output-----
2

Two pairs can be chosen: (2,1) and (2,3).
"""

def count_even_odd_pairs(K: int) -> int:
    """
    Count the number of ways to choose a pair of an even number and an odd number
    from the positive integers between 1 and K (inclusive).

    Parameters:
    K (int): The upper limit of the range (inclusive).

    Returns:
    int: The number of ways to choose such a pair.
    """
    even_count = K // 2
    odd_count = (K + 1) // 2
    return even_count * odd_count