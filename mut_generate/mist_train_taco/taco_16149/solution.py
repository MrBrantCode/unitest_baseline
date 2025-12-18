"""
QUESTION:
You are given four integers $n$, $B$, $x$ and $y$. You should build a sequence $a_0, a_1, a_2, \dots, a_n$ where $a_0 = 0$ and for each $i \ge 1$ you can choose:

either $a_i = a_{i - 1} + x$

or $a_i = a_{i - 1} - y$.

Your goal is to build such a sequence $a$ that $a_i \le B$ for all $i$ and $\sum\limits_{i=0}^{n}{a_i}$ is maximum possible.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases. Next $t$ cases follow.

The first and only line of each test case contains four integers $n$, $B$, $x$ and $y$ ($1 \le n \le 2 \cdot 10^5$; $1 \le B, x, y \le 10^9$).

It's guaranteed that the total sum of $n$ doesn't exceed $2 \cdot 10^5$.


-----Output-----

For each test case, print one integer — the maximum possible $\sum\limits_{i=0}^{n}{a_i}$.


-----Examples-----

Input
3
5 100 1 30
7 1000000000 1000000000 1000000000
4 1 7 3
Output
15
4000000000
-10


-----Note-----

In the first test case, the optimal sequence $a$ is $[0, 1, 2, 3, 4, 5]$.

In the second test case, the optimal sequence $a$ is $[0, 10^9, 0, 10^9, 0, 10^9, 0, 10^9]$.

In the third test case, the optimal sequence $a$ is $[0, -3, -6, 1, -2]$.
"""

def calculate_max_sequence_sum(n: int, B: int, x: int, y: int) -> int:
    """
    Calculate the maximum possible sum of the sequence a_0, a_1, ..., a_n
    where a_0 = 0 and for each i >= 1, a_i can be either a_{i-1} + x or a_{i-1} - y,
    subject to the constraint that a_i <= B for all i.

    Parameters:
    n (int): The length of the sequence.
    B (int): The upper bound for each element in the sequence.
    x (int): The increment value.
    y (int): The decrement value.

    Returns:
    int: The maximum possible sum of the sequence.
    """
    a = 0
    ans = a
    for i in range(n):
        if a + x <= B:
            a += x
        else:
            a -= y
        ans += a
    return ans