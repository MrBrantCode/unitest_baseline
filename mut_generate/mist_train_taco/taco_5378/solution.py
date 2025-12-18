"""
QUESTION:
n people came to a party. Then those, who had no friends among people at the party, left. Then those, who had exactly 1 friend among those who stayed, left as well. Then those, who had exactly 2, 3, ..., n - 1 friends among those who stayed by the moment of their leaving, did the same.

What is the maximum amount of people that could stay at the party in the end? 

Input

The first input line contains one number t — amount of tests (1 ≤ t ≤ 105). Each of the following t lines contains one integer number n (1 ≤ n ≤ 105).

Output

For each test output in a separate line one number — the maximum amount of people that could stay in the end.

Examples

Input

1
3


Output

1
"""

def calculate_max_stay(n: int) -> int:
    """
    Calculate the maximum number of people that could stay at the party in the end.

    Parameters:
    n (int): The number of people at the party.

    Returns:
    int: The maximum number of people that could stay at the party in the end.
    """
    return max(0, n - 2)