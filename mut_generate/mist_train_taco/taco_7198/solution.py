"""
QUESTION:
Some time ago Mister B detected a strange signal from the space, which he started to study.

After some transformation the signal turned out to be a permutation p of length n or its cyclic shift. For the further investigation Mister B need some basis, that's why he decided to choose cyclic shift of this permutation which has the minimum possible deviation.

Let's define the deviation of a permutation p as $\sum_{i = 1}^{i = n}|p [ i ] - i|$.

Find a cyclic shift of permutation p with minimum possible deviation. If there are multiple solutions, print any of them.

Let's denote id k (0 ≤ k < n) of a cyclic shift of permutation p as the number of right shifts needed to reach this shift, for example:

  k = 0: shift p_1, p_2, ... p_{n},  k = 1: shift p_{n}, p_1, ... p_{n} - 1,  ...,  k = n - 1: shift p_2, p_3, ... p_{n}, p_1. 


-----Input-----

First line contains single integer n (2 ≤ n ≤ 10^6) — the length of the permutation.

The second line contains n space-separated integers p_1, p_2, ..., p_{n} (1 ≤ p_{i} ≤ n) — the elements of the permutation. It is guaranteed that all elements are distinct.


-----Output-----

Print two integers: the minimum deviation of cyclic shifts of permutation p and the id of such shift. If there are multiple solutions, print any of them.


-----Examples-----
Input
3
1 2 3

Output
0 0

Input
3
2 3 1

Output
0 1

Input
3
3 2 1

Output
2 1



-----Note-----

In the first sample test the given permutation p is the identity permutation, that's why its deviation equals to 0, the shift id equals to 0 as well.

In the second sample test the deviation of p equals to 4, the deviation of the 1-st cyclic shift (1, 2, 3) equals to 0, the deviation of the 2-nd cyclic shift (3, 1, 2) equals to 4, the optimal is the 1-st cyclic shift.

In the third sample test the deviation of p equals to 4, the deviation of the 1-st cyclic shift (1, 3, 2) equals to 2, the deviation of the 2-nd cyclic shift (2, 1, 3) also equals to 2, so the optimal are both 1-st and 2-nd cyclic shifts.
"""

def find_min_deviation_shift(n, p):
    res = 0
    ires = 0
    neg = 0
    when = [0] * n
    
    # Transform the permutation to calculate initial deviation
    for i in range(n):
        p[i] = i + 1 - p[i]
        res += abs(p[i])
        if p[i] <= 0:
            neg += 1
        a = -p[i]
        if a < 0:
            a = a + n
        when[a] += 1
    
    ares = res
    
    # Calculate the deviation for each cyclic shift
    for i in range(n):
        neg -= when[i]
        ares -= neg
        ares += n - neg
        x = p[n - i - 1] + i + 1
        ares -= x
        ares += n - x
        neg += 1
        if ares < res:
            res = ares
            ires = i + 1
    
    return res, ires