"""
QUESTION:
Ksenia has an array $a$ consisting of $n$ positive integers $a_1, a_2, \ldots, a_n$. 

In one operation she can do the following:   choose three distinct indices $i$, $j$, $k$, and then  change all of $a_i, a_j, a_k$ to $a_i \oplus a_j \oplus a_k$ simultaneously, where $\oplus$ denotes the bitwise XOR operation. 

She wants to make all $a_i$ equal in at most $n$ operations, or to determine that it is impossible to do so. She wouldn't ask for your help, but please, help her!


-----Input-----

The first line contains one integer $n$ ($3 \leq n \leq 10^5$) — the length of $a$.

The second line contains $n$ integers, $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq 10^9$) — elements of $a$.


-----Output-----

Print YES or NO in the first line depending on whether it is possible to make all elements equal in at most $n$ operations.

If it is possible, print an integer $m$ ($0 \leq m \leq n$), which denotes the number of operations you do.

In each of the next $m$ lines, print three distinct integers $i, j, k$, representing one operation. 

If there are many such operation sequences possible, print any. Note that you do not have to minimize the number of operations.


-----Examples-----
Input
5
4 2 1 7 2

Output
YES
1
1 3 4
Input
4
10 4 49 22

Output
NO



-----Note-----

In the first example, the array becomes $[4 \oplus 1 \oplus 7, 2, 4 \oplus 1 \oplus 7, 4 \oplus 1 \oplus 7, 2] = [2, 2, 2, 2, 2]$.
"""

def can_make_elements_equal(n, a):
    if n % 2 == 1:
        operations = []
        for j in range(1, n - 1, 2):
            operations.append((j, j + 1, j + 2))
        for j in range(n - 4, 0, -2):
            operations.append((j, j + 1, j + 2))
        return "YES", len(operations), operations
    
    x = a[0] ^ a[1] ^ a[2]
    y = 0
    for j in range(3, n):
        y ^= a[j]
    
    if x != y:
        return "NO", 0, []
    
    operations = [(1, 2, 3)]
    for j in range(4, n - 1, 2):
        operations.append((j, j + 1, j + 2))
    for j in range(n - 4, 3, -2):
        operations.append((j, j + 1, j + 2))
    
    return "YES", 1 + (n - 5 if n > 4 else 0), operations