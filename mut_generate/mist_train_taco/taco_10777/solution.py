"""
QUESTION:
Read problems statements in [Hindi], [Mandarin Chinese], [Russian], [Vietnamese], and [Bengali] as well.

You are given a range of integers $\{L, L+1, \ldots, R\}$. An integer $X$ is said to be *reachable* if it can be represented as a sum of two not necessarily distinct integers in this range. Find the number of distinct reachable integers.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains two space-separated integers $L$ and $R$.

------  Output ------
For each test case, print a single line containing one integer — the number of reachable integers.

------  Constraints ------
$1 ≤ T ≤ 10^{5}$
$1 ≤ L ≤ R ≤ 10^{6}$

----- Sample Input 1 ------ 
2

2 2

2 3
----- Sample Output 1 ------ 
1

3
----- explanation 1 ------ 
Example case 1: The only reachable integer is $2 + 2 = 4$.

Example case 2: $4$, $5$ and $6$ are reachable, since $2+2=4$, $2+3=5$ and $3+3=6$.
"""

def count_reachable_integers(L: int, R: int) -> int:
    """
    Calculate the number of distinct reachable integers in the range [L, R].

    An integer X is reachable if it can be represented as a sum of two not necessarily distinct integers in the range [L, R].

    Parameters:
    L (int): The lower bound of the range.
    R (int): The upper bound of the range.

    Returns:
    int: The number of distinct reachable integers.
    """
    # Adjust the range to consider sums of two integers
    L = 2 * L
    R = 2 * R
    
    # The number of distinct reachable integers is the difference between the adjusted bounds plus one
    return R - L + 1