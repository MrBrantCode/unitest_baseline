"""
QUESTION:
Dima the hamster enjoys nibbling different things: cages, sticks, bad problemsetters and even trees!

Recently he found a binary search tree and instinctively nibbled all of its edges, hence messing up the vertices. Dima knows that if Andrew, who has been thoroughly assembling the tree for a long time, comes home and sees his creation demolished, he'll get extremely upset. 

To not let that happen, Dima has to recover the binary search tree. Luckily, he noticed that any two vertices connected by a direct edge had their greatest common divisor value exceed $1$.

Help Dima construct such a binary search tree or determine that it's impossible. The definition and properties of a binary search tree can be found here.


-----Input-----

The first line contains the number of vertices $n$ ($2 \le n \le 700$).

The second line features $n$ distinct integers $a_i$ ($2 \le a_i \le 10^9$) — the values of vertices in ascending order.


-----Output-----

If it is possible to reassemble the binary search tree, such that the greatest common divisor of any two vertices connected by the edge is greater than $1$, print "Yes" (quotes for clarity).

Otherwise, print "No" (quotes for clarity).


-----Examples-----
Input
6
3 6 9 18 36 108

Output
Yes

Input
2
7 17

Output
No

Input
9
4 8 10 12 15 18 33 44 81

Output
Yes



-----Note-----

The picture below illustrates one of the possible trees for the first example. [Image] 

The picture below illustrates one of the possible trees for the third example. [Image]
"""

from math import gcd

def can_construct_bst(n: int, a: list) -> bool:
    """
    Determines if it is possible to construct a binary search tree from the given vertices
    such that the greatest common divisor of any two vertices connected by an edge is greater than 1.

    Parameters:
    n (int): The number of vertices.
    a (list): A list of distinct integers representing the values of the vertices in ascending order.

    Returns:
    bool: True if it is possible to construct the binary search tree, False otherwise.
    """
    GCD = [1 << i for i in range(n + 1)]
    for i in range(n):
        for j in range(i):
            if gcd(a[i], a[j]) > 1:
                GCD[i] += 1 << j
                GCD[j] += 1 << i
    
    check1 = [1 << j for j in range(n + 1)]
    check2 = [1 << j for j in range(n + 1)]
    
    for i in range(n):
        check1[0] |= int(bool(check1[0] & check2[i] & GCD[i + 1])) * (1 << i + 1)
        for j in range(1, n - i):
            check1[j] |= int(bool(check1[j] & check2[i + j] & GCD[j + i + 1])) * (1 << i + j + 1)
            check2[j + i] |= int(bool(check1[j] & check2[i + j] & GCD[j - 1])) * (1 << j - 1)
    
    ans = bool(check1[0] & check2[n - 1])
    return ans