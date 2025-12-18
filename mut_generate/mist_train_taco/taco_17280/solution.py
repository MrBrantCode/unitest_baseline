"""
QUESTION:
You are given a range of positive integers from $l$ to $r$.

Find such a pair of integers $(x, y)$ that $l \le x, y \le r$, $x \ne y$ and $x$ divides $y$.

If there are multiple answers, print any of them.

You are also asked to answer $T$ independent queries.


-----Input-----

The first line contains a single integer $T$ ($1 \le T \le 1000$) — the number of queries.

Each of the next $T$ lines contains two integers $l$ and $r$ ($1 \le l \le r \le 998244353$) — inclusive borders of the range.

It is guaranteed that testset only includes queries, which have at least one suitable pair.


-----Output-----

Print $T$ lines, each line should contain the answer — two integers $x$ and $y$ such that $l \le x, y \le r$, $x \ne y$ and $x$ divides $y$. The answer in the $i$-th line should correspond to the $i$-th query from the input.

If there are multiple answers, print any of them.


-----Example-----
Input
3
1 10
3 14
1 10

Output
1 7
3 9
5 10
"""

def find_divisible_pair(l, r):
    """
    Finds a pair of integers (x, y) such that l <= x, y <= r, x != y, and x divides y.

    Parameters:
    l (int): The lower bound of the range (inclusive).
    r (int): The upper bound of the range (inclusive).

    Returns:
    tuple: A tuple (x, y) where x divides y.
    """
    x = l
    y = 2 * l
    return (x, y)