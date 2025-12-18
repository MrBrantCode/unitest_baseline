"""
QUESTION:
You are given three integers $a$, $b$, and $c$. Determine if one of them is the sum of the other two.


-----Input-----

The first line contains a single integer $t$ ($1 \leq t \leq 9261$) — the number of test cases.

The description of each test case consists of three integers $a$, $b$, $c$ ($0 \leq a, b, c \leq 20$).


-----Output-----

For each test case, output "YES" if one of the numbers is the sum of the other two, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).


-----Examples-----

Input
7
1 4 3
2 5 8
9 11 20
0 0 0
20 20 20
4 12 3
15 7 8
Output
YES
NO
YES
YES
NO
NO
YES


-----Note-----

In the first test case, $1 + 3 = 4$.

In the second test case, none of the numbers is the sum of the other two.

In the third test case, $9 + 11 = 20$.
"""

def is_sum_of_two(a: int, b: int, c: int) -> str:
    """
    Determines if one of the given integers is the sum of the other two.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.
    c (int): The third integer.

    Returns:
    str: "YES" if one of the numbers is the sum of the other two, "NO" otherwise.
    """
    l = sorted([a, b, c])
    if l[0] + l[1] == l[2]:
        return "YES"
    else:
        return "NO"