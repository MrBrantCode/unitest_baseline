"""
QUESTION:
Chef was bored staying at home in the lockdown. He wanted to go out for a change. Chef and Chefu are fond of eating Cakes,so they decided to go the Cake shop where cakes of all possible price are available .
They decided to purchase cakes of equal price and each of them will pay for their cakes. Chef only has coins of denomination $N$ whereas Chefu has that of denomination $M$.
So they want your help to find out the minimum amount to be spent in order to purchase the cakes.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input, two integers $N, M$. 

-----Output:-----
For each testcase, output in a single line answer the minimum amount to be spent in order to purchase the cake.

-----Constraints-----
- $1 \leq T \leq 1000$
- $2 \leq N,M \leq 10^7$

-----Sample Input:-----
1
2 3

-----Sample Output:-----
6
"""

import math

def calculate_minimum_cake_price(N, M):
    """
    Calculate the minimum amount to be spent in order to purchase cakes
    where Chef has coins of denomination N and Chefu has coins of denomination M.

    Parameters:
    - N (int): Denomination of Chef's coins.
    - M (int): Denomination of Chefu's coins.

    Returns:
    - int: The minimum amount to be spent.
    """
    return (N * M) // math.gcd(N, M)