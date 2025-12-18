"""
QUESTION:
Theofanis has a riddle for you and if you manage to solve it, he will give you a Cypriot snack halloumi for free (Cypriot cheese).

You are given an integer $n$. You need to find two integers $l$ and $r$ such that $-10^{18} \le l < r \le 10^{18}$ and $l + (l + 1) + \ldots + (r - 1) + r = n$.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases.

The first and only line of each test case contains a single integer $n$ ($1 \le n \le 10^{18}$).


-----Output-----

For each test case, print the two integers $l$ and $r$ such that $-10^{18} \le l < r \le 10^{18}$ and $l + (l + 1) + \ldots + (r - 1) + r = n$.

It can be proven that an answer always exists. If there are multiple answers, print any.


-----Examples-----

Input
7
1
2
3
6
100
25
3000000000000
Output
0 1
-1 2 
1 2 
1 3 
18 22
-2 7
999999999999 1000000000001


-----Note-----

In the first test case, $0 + 1 = 1$.

In the second test case, $(-1) + 0 + 1 + 2 = 2$.

In the fourth test case, $1 + 2 + 3 = 6$.

In the fifth test case, $18 + 19 + 20 + 21 + 22 = 100$.

In the sixth test case, $(-2) + (-1) + 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 = 25$.
"""

def find_lr_pair(n: int) -> tuple:
    """
    Finds two integers l and r such that l + (l + 1) + ... + (r - 1) + r = n.

    Parameters:
    n (int): The target sum.

    Returns:
    tuple: A tuple (l, r) where l and r satisfy the condition.
    """
    l = -n + 1
    r = n
    return (l, r)