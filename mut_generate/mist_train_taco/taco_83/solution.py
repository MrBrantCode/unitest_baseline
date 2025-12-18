"""
QUESTION:
The sum of digits of a non-negative integer $a$ is the result of summing up its digits together when written in the decimal system. For example, the sum of digits of $123$ is $6$ and the sum of digits of $10$ is $1$. In a formal way, the sum of digits of $\displaystyle a=\sum_{i=0}^{\infty} a_i \cdot 10^i$, where $0 \leq a_i \leq 9$, is defined as $\displaystyle\sum_{i=0}^{\infty}{a_i}$.

Given an integer $n$, find two non-negative integers $x$ and $y$ which satisfy the following conditions.

$x+y=n$, and

the sum of digits of $x$ and the sum of digits of $y$ differ by at most $1$.

It can be shown that such $x$ and $y$ always exist.


-----Input-----

Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \le t \le 10000$).

Each test case consists of a single integer $n$ ($1 \leq n \leq 10^9$)


-----Output-----

For each test case, print two integers $x$ and $y$.

If there are multiple answers, print any.


-----Examples-----

Input
5
1
161
67
1206
19
Output
1 0
67 94
60 7
1138 68
14 5


-----Note-----

In the second test case, the sum of digits of $67$ and the sum of digits of $94$ are both $13$.

In the third test case, the sum of digits of $60$ is $6$, and the sum of digits of $7$ is $7$.
"""

def find_xy_with_close_digit_sums(n: int) -> tuple:
    """
    Finds two non-negative integers x and y such that:
    1. x + y = n
    2. The sum of digits of x and the sum of digits of y differ by at most 1.

    Parameters:
    n (int): The given integer for which to find x and y.

    Returns:
    tuple: A tuple containing two integers (x, y).
    """
    s = ''
    s1 = ''
    c = 1
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            s = str(d // 2) + s
            s1 = str(d // 2) + s1
        elif c == 1:
            s = str(d // 2) + s
            s1 = str(d // 2 + 1) + s1
            c -= 1
        else:
            s = str(d // 2 + 1) + s
            s1 = str(d // 2) + s1
            c += 1
        n = n // 10
    return (int(s), int(s1))