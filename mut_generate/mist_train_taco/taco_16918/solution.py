"""
QUESTION:
In winter, the inhabitants of the Moscow Zoo are very bored, in particular, it concerns gorillas. You decided to entertain them and brought a permutation $p$ of length $n$ to the zoo.

A permutation of length $n$ is an array consisting of $n$ distinct integers from $1$ to $n$ in any order. For example, $[2,3,1,5,4]$ is a permutation, but $[1,2,2]$ is not a permutation ($2$ occurs twice in the array) and $[1,3,4]$ is also not a permutation ($n=3$, but $4$ is present in the array).

The gorillas had their own permutation $q$ of length $n$. They suggested that you count the number of pairs of integers $l, r$ ($1 \le l \le r \le n$) such that $\operatorname{MEX}([p_l, p_{l+1}, \ldots, p_r])=\operatorname{MEX}([q_l, q_{l+1}, \ldots, q_r])$.

The $\operatorname{MEX}$ of the sequence is the minimum integer positive number missing from this sequence. For example, $\operatorname{MEX}([1, 3]) = 2$, $\operatorname{MEX}([5]) = 1$, $\operatorname{MEX}([3, 1, 2, 6]) = 4$.

You do not want to risk your health, so you will not dare to refuse the gorillas.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^5$) — the permutations length.

The second line contains $n$ integers $p_1, p_2, \ldots, p_n$ ($1 \le p_i \le n$) — the elements of the permutation $p$.

The third line contains $n$ integers $q_1, q_2, \ldots, q_n$ ($1 \le q_i \le n$) — the elements of the permutation $q$.


-----Output-----

Print a single integer — the number of suitable pairs $l$ and $r$.


-----Examples-----

Input
3
1 3 2
2 1 3
Output
2
Input
7
7 3 6 2 1 5 4
6 7 2 5 3 1 4
Output
16
Input
6
1 2 3 4 5 6
6 5 4 3 2 1
Output
11


-----Note-----

In the first example, two segments are correct – $[1, 3]$ with $\operatorname{MEX}$ equal to $4$ in both arrays and $[3, 3]$ with $\operatorname{MEX}$ equal to $1$ in both of arrays.

In the second example, for example, the segment $[1, 4]$ is correct, and the segment $[6, 7]$ isn't correct, because $\operatorname{MEX}(5, 4) \neq \operatorname{MEX}(1, 4)$.
"""

def count_matching_mex_pairs(n, p, q):
    """
    Counts the number of pairs of integers (l, r) such that the MEX of the subarrays 
    [p_l, p_{l+1}, ..., p_r] and [q_l, q_{l+1}, ..., q_r] are equal.

    Parameters:
    n (int): The length of the permutations.
    p (list of int): The first permutation.
    q (list of int): The second permutation.

    Returns:
    int: The number of suitable pairs (l, r).
    """
    pi = [None] * (n + 1)
    qi = [None] * (n + 1)
    for i in range(n):
        pi[p[i]] = i
        qi[q[i]] = i
    
    x = pi[1]
    y = qi[1]
    if x > y:
        (x, y) = (y, x)
    
    res = 0
    if x >= 1:
        res += x * (x + 1) // 2
    if n - 1 - y >= 1:
        res += (n - y - 1) * (n - y) // 2
    if y - x - 1 >= 1:
        res += (y - x - 1) * (y - x) // 2
    
    l = x
    r = y
    for i in range(2, n):
        x = pi[i]
        y = qi[i]
        if x > y:
            (x, y) = (y, x)
        if not (x >= l and x <= r or (y >= l and y <= r)):
            if y < l:
                u = l - y
            elif x < l:
                u = l - x
            else:
                u = l + 1
            if x > r:
                v = x - r
            elif y > r:
                v = y - r
            else:
                v = n - r
            res += u * v
        l = min(l, x)
        r = max(r, y)
    
    return res + 1