"""
QUESTION:
Your task is to calculate the number of arrays such that:  each array contains $n$ elements;  each element is an integer from $1$ to $m$;  for each array, there is exactly one pair of equal elements;  for each array $a$, there exists an index $i$ such that the array is strictly ascending before the $i$-th element and strictly descending after it (formally, it means that $a_j < a_{j + 1}$, if $j < i$, and $a_j > a_{j + 1}$, if $j \ge i$). 


-----Input-----

The first line contains two integers $n$ and $m$ ($2 \le n \le m \le 2 \cdot 10^5$).


-----Output-----

Print one integer — the number of arrays that meet all of the aforementioned conditions, taken modulo $998244353$.


-----Examples-----
Input
3 4

Output
6

Input
3 5

Output
10

Input
42 1337

Output
806066790

Input
100000 200000

Output
707899035



-----Note-----

The arrays in the first example are:  $[1, 2, 1]$;  $[1, 3, 1]$;  $[1, 4, 1]$;  $[2, 3, 2]$;  $[2, 4, 2]$;  $[3, 4, 3]$.
"""

def count_valid_arrays(n, m, mod=998244353):
    # Precompute factorials modulo mod
    frac = [1] * (m + 1)
    for i in range(1, m + 1):
        frac[i] = frac[i - 1] * i % mod

    # Function to compute binomial coefficient C(a, b) modulo mod
    def C(a, b):
        return frac[a] * pow(frac[a - b], mod - 2, mod) % mod * pow(frac[b], mod - 2, mod) % mod

    # Calculate p
    p = 0
    for i in range(n - 1):
        p = (p + C(n - 2, i)) % mod

    # Calculate the final answer
    ans = 0
    for i in range(m, n - 2, -1):
        ans = (ans + C(i - 1, n - 2) * (n - 2) * p // 2) % mod

    return ans