"""
QUESTION:
You are given an integer $n$.

Let's define $s(n)$ as the string "BAN" concatenated $n$ times. For example, $s(1)$ = "BAN", $s(3)$ = "BANBANBAN". Note that the length of the string $s(n)$ is equal to $3n$.

Consider $s(n)$. You can perform the following operation on $s(n)$ any number of times (possibly zero):

Select any two distinct indices $i$ and $j$ $(1 \leq i, j \leq 3n, i \ne j)$.

Then, swap $s(n)_i$ and $s(n)_j$.

You want the string "BAN" to not appear in $s(n)$ as a subsequence. What's the smallest number of operations you have to do to achieve this? Also, find one such shortest sequence of operations.

A string $a$ is a subsequence of a string $b$ if $a$ can be obtained from $b$ by deletion of several (possibly, zero or all) characters.


-----Input-----

The input consists of multiple test cases. The first line contains a single integer $t$ $(1 \leq t \leq 100)$  — the number of test cases. The description of the test cases follows.

The only line of each test case contains a single integer $n$ $(1 \leq n \leq 100)$.


-----Output-----

For each test case, in the first line output $m$ ($0 \le m \le 10^5$) — the minimum number of operations required. It's guaranteed that the objective is always achievable in at most $10^5$ operations under the constraints of the problem.

Then, output $m$ lines. The $k$-th of these lines should contain two integers $i_k$, $j_k$ $(1\leq i_k, j_k \leq 3n, i_k \ne j_k)$ denoting that you want to swap characters at indices $i_k$ and $j_k$ at the $k$-th operation.

After all $m$ operations, "BAN" must not appear in $s(n)$ as a subsequence.

If there are multiple possible answers, output any.


-----Examples-----

Input
2
1
2
Output
1
1 2
1
2 6


-----Note-----

In the first testcase, $s(1) = $ "BAN", we can swap $s(1)_1$ and $s(1)_2$, converting $s(1)$ to "ABN", which does not contain "BAN" as a subsequence.

In the second testcase, $s(2) = $ "BANBAN", we can swap $s(2)_2$ and $s(2)_6$, converting $s(2)$ to "BNNBAA", which does not contain "BAN" as a subsequence.
"""

def min_operations_to_remove_subsequence(n: int) -> (int, list):
    """
    Calculate the minimum number of operations required to ensure that the string "BAN" does not appear as a subsequence
    in the string formed by concatenating "BAN" n times. Also, return the sequence of operations.

    :param n: An integer representing the number of times the string "BAN" is concatenated.
    :return: A tuple containing:
             - m: An integer representing the minimum number of operations required.
             - operations: A list of tuples, where each tuple contains two integers representing the indices to swap in each operation.
    """
    m = n // 2 + n % 2
    operations = []
    l = 1
    r = 3 * n
    
    while r > l:
        operations.append((l, r))
        l += 3
        r -= 3
    
    return m, operations