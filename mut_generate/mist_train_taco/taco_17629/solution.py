"""
QUESTION:
There is an array $a$ of length $n$. You may perform the following operation any number of times:

Choose two indices $l$ and $r$ where $1 \le l < r \le n$ and $a_l = a_r$. Then, set $a[l \ldots r] = [a_{l+1}, a_{l+2}, \ldots, a_r, a_l]$.

You are also given another array $b$ of length $n$ which is a permutation of $a$. Determine whether it is possible to transform array $a$ into an array $b$ using the above operation some number of times.


-----Input-----

Each test contains multiple test cases. The first line contains a single integer $t$ ($1 \leq t \leq 10^4$)  — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer $n$ ($1 \le n \le 2 \cdot 10 ^ 5$)  — the length of array $a$ and $b$.

The second line of each test case contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le n$)  — elements of the array $a$.

The third line of each test case contains $n$ integers $b_1, b_2, \ldots, b_n$ ($1 \le b_i \le n$)  — elements of the array $b$.

It is guaranteed that $b$ is a permutation of $a$.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10 ^ 5$


-----Output-----

For each test case, print "YES" (without quotes) if it is possible to transform array $a$ to $b$, and "NO" (without quotes) otherwise.

You can output "YES" and "NO" in any case (for example, strings "yEs", "yes" and "Yes" will be recognized as a positive response).


-----Examples-----

Input
5
5
1 2 3 3 2
1 3 3 2 2
5
1 2 4 2 1
4 2 2 1 1
5
2 4 5 5 2
2 2 4 5 5
3
1 2 3
1 2 3
3
1 1 2
2 1 1
Output
YES
YES
NO
YES
NO


-----Note-----

In the first test case, we can choose $l=2$ and $r=5$ to form $[1, 3, 3, 2, 2]$.

In the second test case, we can choose $l=2$ and $r=4$ to form $[1, 4, 2, 2, 1]$. Then, we can choose $l=1$ and $r=5$ to form $[4, 2, 2, 1, 1]$.

In the third test case, it can be proven that it is not possible to transform array $a$ to $b$ using the operation.
"""

def can_transform_to_permutation(a: list, b: list) -> bool:
    """
    Determines whether it is possible to transform array `a` into array `b` using the specified operation.

    Parameters:
    - a (list): The initial array.
    - b (list): The target permutation array.

    Returns:
    - bool: True if it is possible to transform `a` into `b`, False otherwise.
    """
    n = len(a)
    if n != len(b):
        return False
    
    w = [0] * (n + 1)
    j = 0
    
    for i in range(n):
        x = b[i]
        while j < n and a[j] != x:
            w[a[j]] += 1
            j += 1
        if j == n:
            return False
        if i + 1 < n and b[i + 1] == x:
            if j + 1 >= n or a[j + 1] != x:
                if w[x] > 0:
                    w[x] -= 1
                    i += 1
                    continue
        j += 1
    
    return True