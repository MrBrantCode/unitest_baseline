"""
QUESTION:
On a random day, Neko found $n$ treasure chests and $m$ keys. The $i$-th chest has an integer $a_i$ written on it and the $j$-th key has an integer $b_j$ on it. Neko knows those chests contain the powerful mysterious green Grapes, thus Neko wants to open as many treasure chests as possible.

The $j$-th key can be used to unlock the $i$-th chest if and only if the sum of the key number and the chest number is an odd number. Formally, $a_i + b_j \equiv 1 \pmod{2}$. One key can be used to open at most one chest, and one chest can be opened at most once.

Find the maximum number of chests Neko can open.


-----Input-----

The first line contains integers $n$ and $m$ ($1 \leq n, m \leq 10^5$) — the number of chests and the number of keys.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq 10^9$) — the numbers written on the treasure chests.

The third line contains $m$ integers $b_1, b_2, \ldots, b_m$ ($1 \leq b_i \leq 10^9$) — the numbers written on the keys.


-----Output-----

Print the maximum number of chests you can open.


-----Examples-----
Input
5 4
9 14 6 2 11
8 4 7 20

Output
3
Input
5 1
2 4 6 8 10
5

Output
1
Input
1 4
10
20 30 40 50

Output
0


-----Note-----

In the first example, one possible way to unlock $3$ chests is as follows:

  Use first key to unlock the fifth chest,  Use third key to unlock the second chest,  Use fourth key to unlock the first chest. 

In the second example, you can use the only key to unlock any single chest (note that one key can't be used twice).

In the third example, no key can unlock the given chest.
"""

def max_chests_opened(n: int, m: int, a: list[int], b: list[int]) -> int:
    """
    Calculate the maximum number of treasure chests that can be opened with the given keys.

    Parameters:
    n (int): The number of treasure chests.
    m (int): The number of keys.
    a (list[int]): The list of integers written on the treasure chests.
    b (list[int]): The list of integers written on the keys.

    Returns:
    int: The maximum number of chests that can be opened.
    """
    odd_a = sum(1 for x in a if x % 2)
    odd_b = sum(1 for x in b if x % 2)
    even_a = n - odd_a
    even_b = m - odd_b
    return min(odd_a, even_b) + min(even_a, odd_b)