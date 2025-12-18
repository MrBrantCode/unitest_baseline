"""
QUESTION:
This is the hard version of this problem. In this version, $n \le 5000$ holds, and this version has no restriction between $x$ and $y$. You can make hacks only if both versions of the problem are solved.

You are given two binary strings $a$ and $b$, both of length $n$. You can do the following operation any number of times (possibly zero).

Select two indices $l$ and $r$ ($l < r$).

Change $a_l$ to $(1 - a_l)$, and $a_r$ to $(1 - a_r)$.

If $l + 1 = r$, the cost of the operation is $x$. Otherwise, the cost is $y$.

You have to find the minimum cost needed to make $a$ equal to $b$ or say there is no way to do so.


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 1000$) — the number of test cases.

Each test case consists of three lines. The first line of each test case contains three integers $n$, $x$, and $y$ ($5 \le n \le 5000$, $1 \le x, y \le 10^9$) — the length of the strings, and the costs per operation.

The second line of each test case contains the string $a$ of length $n$. The string only consists of digits $0$ and $1$.

The third line of each test case contains the string $b$ of length $n$. The string only consists of digits $0$ and $1$.

It is guaranteed that the sum of $n$ over all test cases doesn't exceed $5000$.


-----Output-----

For each test case, if there is no way to make $a$ equal to $b$, print $-1$. Otherwise, print the minimum cost needed to make $a$ equal to $b$.


-----Examples-----

Input
6
5 8 9
01001
00101
6 2 11
000001
100000
5 7 2
01000
11011
7 8 3
0111001
0100001
6 3 4
010001
101000
5 10 1
01100
01100
Output
8
10
-1
6
7
0


-----Note-----

In the first test case, selecting indices $2$ and $3$ costs $8$, which is the minimum.

In the second test case, we can perform the following operations.

Select indices $1$ and $2$. It costs $2$, and $a$ is 110001 now.

Select indices $2$ and $3$. It costs $2$, and $a$ is 101001 now.

Select indices $3$ and $4$. It costs $2$, and $a$ is 100101 now.

Select indices $4$ and $5$. It costs $2$, and $a$ is 100011 now.

Select indices $5$ and $6$. It costs $2$, and $a$ is 100000 now.

The total cost is $10$.

In the third test case, we cannot make $a$ equal to $b$ using any number of operations.

In the fourth test case, we can perform the following operations.

Select indices $3$ and $6$. It costs $3$, and $a$ is 0101011 now.

Select indices $4$ and $6$. It costs $3$, and $a$ is 0100001 now.

The total cost is $6$.

In the fifth test case, we can perform the following operations.

Select indices $1$ and $6$. It costs $4$, and $a$ is 110000 now.

Select indices $2$ and $3$. It costs $3$, and $a$ is 101000 now.

The total cost is $7$.

In the sixth test case, we don't have to perform any operation.
"""

def min_cost_to_equalize_binary_strings(n, x, y, a, b):
    """
    Calculate the minimum cost needed to make binary string `a` equal to binary string `b`
    using the specified operations.

    Parameters:
    - n (int): The length of the binary strings.
    - x (int): The cost for an operation where `l + 1 = r`.
    - y (int): The cost for an operation where `l + 1 != r`.
    - a (str): The first binary string.
    - b (str): The second binary string.

    Returns:
    - int: The minimum cost needed to make `a` equal to `b`, or `-1` if it's not possible.
    """
    # Find indices where `a` and `b` differ
    zs = [i for i, (c, d) in enumerate(zip(a, b)) if c != d]
    
    # If the number of differing positions is odd, it's impossible to make `a` equal to `b`
    if len(zs) % 2 != 0:
        return -1
    
    # If there are no differing positions, no cost is needed
    if len(zs) == 0:
        return 0
    
    # If x is greater than or equal to y, handle the special case where len(zs) == 2 and zs[0] + 1 == zs[1]
    if x >= y:
        if len(zs) == 2 and zs[0] + 1 == zs[1]:
            return min(x, 2 * y)
        else:
            return len(zs) // 2 * y
    
    # If x is less than y, use dynamic programming to find the minimum cost
    f = []
    for i, z in enumerate(zs):
        if i == 0:
            cur = y
        elif i == 1:
            cur = min(2 * y, 2 * x * (z - zs[0]))
        else:
            cur = min(2 * x * (z - zs[i - 1]) + f[i - 2], y + f[i - 1])
        f.append(cur)
    
    return f[-1] // 2