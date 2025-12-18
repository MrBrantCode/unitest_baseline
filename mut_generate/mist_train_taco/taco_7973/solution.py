"""
QUESTION:
Alice has a cake, and she is going to cut it. She will perform the following operation $n-1$ times: choose a piece of the cake (initially, the cake is all one piece) with weight $w\ge 2$ and cut it into two smaller pieces of weight $\lfloor\frac{w}{2}\rfloor$ and $\lceil\frac{w}{2}\rceil$ ($\lfloor x \rfloor$ and $\lceil x \rceil$ denote floor and ceiling functions , respectively).

After cutting the cake in $n$ pieces, she will line up these $n$ pieces on a table in an arbitrary order. Let $a_i$ be the weight of the $i$-th piece in the line.

You are given the array $a$. Determine whether there exists an initial weight and sequence of operations which results in $a$.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 10^4$) — the number of test cases.

The first line of each test case contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$).

The second line of each test case contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 10^9$).

It is guaranteed that the sum of $n$ for all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, print a single line: print YES if the array $a$ could have resulted from Alice's operations, otherwise print NO.

You may print each letter in any case (for example, YES, Yes, yes, yEs will all be recognized as positive answer).


-----Examples-----

Input
14
1
327
2
869 541
2
985214736 985214737
3
2 3 1
3
2 3 3
6
1 1 1 1 1 1
6
100 100 100 100 100 100
8
100 100 100 100 100 100 100 100
8
2 16 1 8 64 1 4 32
10
1 2 4 7 1 1 1 1 7 2
10
7 1 1 1 3 1 3 3 2 3
10
1 4 4 1 1 1 3 3 3 1
10
2 3 2 2 1 2 2 2 2 2
4
999999999 999999999 999999999 999999999
Output
YES
NO
YES
YES
NO
YES
NO
YES
YES
YES
YES
NO
NO
YES


-----Note-----

In the first test case, it's possible to get the array $a$ by performing $0$ operations on a cake with weight $327$.

In the second test case, it's not possible to get the array $a$.

In the third test case, it's possible to get the array $a$ by performing $1$ operation on a cake with weight $1\,970\,429\,473$:

Cut it in half, so that the weights are $[985\,214\,736, 985\,214\,737]$.

Note that the starting weight can be greater than $10^9$.

In the fourth test case, it's possible to get the array $a$ by performing $2$ operations on a cake with weight $6$:

Cut it in half, so that the weights are $[3,3]$.

Cut one of the two pieces with weight $3$, so that the new weights are $[1, 2, 3]$ which is equivalent to $[2, 3, 1]$ up to reordering.
"""

def can_form_cake_pieces(n, a):
    """
    Determines whether the given array of cake piece weights can be formed by repeatedly cutting a cake.

    Parameters:
    n (int): The number of pieces of the cake.
    a (list of int): The array representing the weights of the cake pieces.

    Returns:
    bool: True if the array can be formed by Alice's operations, otherwise False.
    """
    from collections import Counter

    def check(val):
        if track[val] > 0:
            track[val] -= 1
            return True
        if val == 1:
            return False
        return check(val // 2) and check((val + 1) // 2)

    track = Counter(a)
    return check(sum(a))