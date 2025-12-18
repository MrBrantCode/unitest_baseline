"""
QUESTION:
Let's call a positive integer extremely round if it has only one non-zero digit. For example, $5000$, $4$, $1$, $10$, $200$ are extremely round integers; $42$, $13$, $666$, $77$, $101$ are not.

You are given an integer $n$. You have to calculate the number of extremely round integers $x$ such that $1 \le x \le n$.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10^4$) — the number of test cases.

Then, $t$ lines follow. The $i$-th of them contains one integer $n$ ($1 \le n \le 999999$) — the description of the $i$-th test case.


-----Output-----

For each test case, print one integer — the number of extremely round integers $x$ such that $1 \le x \le n$.


-----Examples-----

Input
5
9
42
13
100
111
Output
9
13
10
19
19


-----Note-----

None
"""

def count_extremely_round_integers(n: int) -> int:
    """
    Counts the number of extremely round integers between 1 and n (inclusive).

    An extremely round integer is defined as a positive integer that has only one non-zero digit.

    Parameters:
    n (int): The upper limit of the range of integers to check.

    Returns:
    int: The number of extremely round integers between 1 and n.
    """
    count = 0
    for x in range(1, n + 1):
        if len(set(str(x)) - {'0'}) == 1:
            count += 1
    return count