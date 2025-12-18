"""
QUESTION:
You have an array a consisting of n distinct positive integers, numbered from 1 to n. Define p_k as $$$p_k = ∑_{1 ≤ i, j ≤ k} a_i mod a_j, where x \bmod y denotes the remainder when x is divided by y. You have to find and print p_1, p_2, \ldots, p_n$$$. 

Input

The first line contains n — the length of the array (2 ≤ n ≤ 2 ⋅ 10^5).

The second line contains n space-separated distinct integers a_1, …, a_n (1 ≤ a_i ≤ 3 ⋅ 10^5, a_i ≠ a_j if i ≠ j). 

Output

Print n integers p_1, p_2, …, p_n. 

Examples

Input


4
6 2 7 3


Output


0 2 12 22


Input


3
3 2 1


Output


0 3 5
"""

def calculate_p_values(n, a_a):
    def bit_update(bit_a, i, v):
        while i < len(bit_a):
            bit_a[i] += v
            i += i & -i

    def bit_query(bit_a, i):
        r = 0
        while i > 0:
            r += bit_a[i]
            i -= i & -i
        return r

    def bit_range_query(bit_a, l, r):
        return bit_query(bit_a, r) - bit_query(bit_a, l - 1)

    N = max(a_a) + 1
    bit_a = [0 for _ in range(N * 2)]
    bit_a2 = [0 for _ in range(N * 2)]
    p_a = [0] * n
    ans = sum = 0

    for i in range(1, n + 1):
        x = a_a[i - 1]
        ans += x * (i - 1)
        ans += sum
        sum += x
        ans -= bit_query(bit_a, x)
        j = x
        while j < N:
            l = j
            r = l + x - 1
            ans -= bit_range_query(bit_a2, l, r) * j
            bit_update(bit_a, l, x)
            j += x
        bit_update(bit_a2, x, 1)
        p_a[i - 1] = ans

    return p_a