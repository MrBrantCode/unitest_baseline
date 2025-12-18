"""
QUESTION:
oolimry has an array $a$ of length $n$ which he really likes. Today, you have changed his array to $b$, a permutation of $a$, to make him sad.

Because oolimry is only a duck, he can only perform the following operation to restore his array:

Choose two integers $i,j$ such that $1 \leq i,j \leq n$.

Swap $b_i$ and $b_j$.

The sadness of the array $b$ is the minimum number of operations needed to transform $b$ into $a$.

Given the array $a$, find any array $b$ which is a permutation of $a$ that has the maximum sadness over all permutations of the array $a$.


-----Input-----

Each test contains multiple test cases. The first line contains a single integer $t$ ($1 \leq t \leq 10^4$)  — the number of test cases. The description of the test cases follows.

The first line of each test case contains a single integer $n$ ($1 \leq n \leq 2 \cdot 10^5$)  — the length of the array.

The second line of each test case contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \leq a_i \leq n$)  — elements of the array $a$.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, print $n$ integers $b_1, b_2, \ldots, b_n$ — describing the array $b$. If there are multiple answers, you may print any.


-----Examples-----

Input
2
2
2 1
4
1 2 3 3
Output
1 2
3 3 2 1


-----Note-----

In the first test case, the array $[1,2]$ has sadness $1$. We can transform $[1,2]$ into $[2,1]$ using one operation with $(i,j)=(1,2)$.

In the second test case, the array $[3,3,2,1]$ has sadness $2$. We can transform $[3,3,2,1]$ into $[1,2,3,3]$ with two operations with $(i,j)=(1,4)$ and $(i,j)=(2,3)$ respectively.
"""

def find_max_sadness_permutation(n, a):
    """
    Finds a permutation of array `a` that has the maximum sadness.

    Parameters:
    n (int): The length of the array `a`.
    a (list of int): The original array `a`.

    Returns:
    list of int: A permutation of `a` that has the maximum sadness.
    """
    c = [[] for _ in range(n + 1)]
    p = [None] * (n + 1)
    
    for i in range(n):
        c[a[i]].append(i)
    
    for i in range(n + 1):
        p[i] = (-len(c[i]), i)
    
    p.sort()
    
    b = [None] * n
    
    for k in range(-p[0][0]):
        pr = p[0][1]
        for i in range(1, n + 5):
            (sz, v) = p[i]
            if -sz > k:
                b[c[pr][k]] = v
                pr = v
            else:
                b[c[pr][k]] = p[0][1]
                break
    
    return b