"""
QUESTION:
You are given three positive (i.e. strictly greater than zero) integers $x$, $y$ and $z$.

Your task is to find positive integers $a$, $b$ and $c$ such that $x = \max(a, b)$, $y = \max(a, c)$ and $z = \max(b, c)$, or determine that it is impossible to find such $a$, $b$ and $c$.

You have to answer $t$ independent test cases. Print required $a$, $b$ and $c$ in any (arbitrary) order.


-----Input-----

The first line of the input contains one integer $t$ ($1 \le t \le 2 \cdot 10^4$) — the number of test cases. Then $t$ test cases follow.

The only line of the test case contains three integers $x$, $y$, and $z$ ($1 \le x, y, z \le 10^9$).


-----Output-----

For each test case, print the answer:  "NO" in the only line of the output if a solution doesn't exist;  or "YES" in the first line and any valid triple of positive integers $a$, $b$ and $c$ ($1 \le a, b, c \le 10^9$) in the second line. You can print $a$, $b$ and $c$ in any order. 


-----Example-----
Input
5
3 2 3
100 100 100
50 49 49
10 30 20
1 1000000000 1000000000

Output
YES
3 2 1
YES
100 100 100
NO
NO
YES
1 1 1000000000
"""

def find_abc_from_max_pairs(x, y, z):
    """
    Finds positive integers a, b, and c such that x = max(a, b), y = max(a, c), and z = max(b, c),
    or determines that it is impossible to find such a, b, and c.

    Parameters:
    x (int): The first maximum value.
    y (int): The second maximum value.
    z (int): The third maximum value.

    Returns:
    tuple: A tuple containing:
           - A boolean indicating whether a solution exists.
           - If a solution exists, a tuple (a, b, c) with the values of a, b, and c.
           - If no solution exists, None.
    """
    arr = [x, y, z]
    arr.sort()
    
    if arr[-1] == arr[-2]:
        return True, (arr[0], arr[0], arr[-1])
    else:
        return False, None