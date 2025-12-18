"""
QUESTION:
Given an amount A, we want you to compute the number of ways in which you
can gather A rupees if you have an infinite supply of each of C =  {1, 3, 5} valued rupee coins.

Input:

First line contains T, the number of test-cases. This is followed by T lines, where each line consists of the amount A.

Output:

For each test case, print the number of ways in which A can be formed using an infinite supply of 1, 3 and 5 rupee coins.

Constraints

T < 100
A < 101

Explanation :

A = 5

Ways this amount can be achieved: {1,1,1,1,1}, {1,1,3}, {5}
Hence, the answer is 3.

SAMPLE INPUT
2
5
10

SAMPLE OUTPUT
3
7
"""

def count_ways_to_form_amount(amount: int, coins: list) -> int:
    """
    Computes the number of ways to form a given amount using an infinite supply of specified coin denominations.

    Parameters:
    - amount (int): The amount of money to be formed.
    - coins (list of int): The list of coin denominations available.

    Returns:
    - int: The number of ways to form the given amount using the given coin denominations.
    """
    def count(S, m, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        if m <= 0 and n >= 1:
            return 0
        return count(S, m - 1, n) + count(S, m, n - S[m - 1])
    
    return count(coins, len(coins), amount)