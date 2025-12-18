"""
QUESTION:
You are given n integers a_1, a_2, ..., a_{n}. Find the number of pairs of indexes i, j (i < j) that a_{i} + a_{j} is a power of 2 (i. e. some integer x exists so that a_{i} + a_{j} = 2^{x}).


-----Input-----

The first line contains the single positive integer n (1 ≤ n ≤ 10^5) — the number of integers.

The second line contains n positive integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9).


-----Output-----

Print the number of pairs of indexes i, j (i < j) that a_{i} + a_{j} is a power of 2.


-----Examples-----
Input
4
7 3 2 1

Output
2

Input
3
1 1 1

Output
3



-----Note-----

In the first example the following pairs of indexes include in answer: (1, 4) and (2, 4).

In the second example all pairs of indexes (i, j) (where i < j) include in answer.
"""

def count_pairs_with_power_of_two_sum(arr):
    ans = 0
    mp = {}
    
    for i in arr:
        for k in range(32):
            ans += mp.get((1 << k) - i, 0)
        mp[i] = mp.get(i, 0) + 1
    
    return ans