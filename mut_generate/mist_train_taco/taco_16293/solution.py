"""
QUESTION:
Madoka is a very strange girl, and therefore she suddenly wondered how many pairs of integers $(a, b)$ exist, where $1 \leq a, b \leq n$, for which $\frac{\operatorname{lcm}(a, b)}{\operatorname{gcd}(a, b)} \leq 3$.

In this problem, $\operatorname{gcd}(a, b)$ denotes the greatest common divisor of the numbers $a$ and $b$, and $\operatorname{lcm}(a, b)$ denotes the smallest common multiple of the numbers $a$ and $b$.


-----Input-----

The input consists of multiple test cases. The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases. Description of the test cases follows.

The first and the only line of each test case contains the integer $n$ ($1 \le n \le 10^8$).


-----Output-----

For each test case output a single integer — the number of pairs of integers satisfying the condition.


-----Examples-----

Input
6
1
2
3
4
5
100000000
Output
1
4
7
10
11
266666666


-----Note-----

For $n = 1$ there is exactly one pair of numbers — $(1, 1)$ and it fits.

For $n = 2$, there are only $4$ pairs — $(1, 1)$, $(1, 2)$, $(2, 1)$, $(2, 2)$ and they all fit.

For $n = 3$, all $9$ pair are suitable, except $(2, 3)$ and $(3, 2)$, since their $\operatorname{lcm}$ is $6$, and $\operatorname{gcd}$ is $1$, which doesn't fit the condition.
"""

def count_valid_pairs(t: int, n_list: list) -> list:
    """
    Counts the number of pairs (a, b) such that 1 <= a, b <= n and lcm(a, b) / gcd(a, b) <= 3.

    Parameters:
    t (int): The number of test cases.
    n_list (list): A list of integers where each integer represents the value of n for a test case.

    Returns:
    list: A list of integers where each integer represents the number of valid pairs for the corresponding test case.
    """
    results = []
    for n in n_list:
        results.append(n + n // 2 * 2 + n // 3 * 2)
    return results