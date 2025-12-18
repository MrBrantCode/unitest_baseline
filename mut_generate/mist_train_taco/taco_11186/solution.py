"""
QUESTION:
You are given N real values A_1, A_2, \ldots, A_N. Compute the number of pairs of indices (i, j) such that i < j and the product A_i \cdot A_j is integer.

Constraints

* 2 \leq N \leq 200\,000
* 0 < A_i < 10^4
* A_i is given with at most 9 digits after the decimal.

Input

Input is given from Standard Input in the following format.


N
A_1
A_2
\vdots
A_N


Output

Print the number of pairs with integer product A_i \cdot A_j (and i < j).

Examples

Input

5
7.5
2.4
17.000000001
17
16.000000000


Output

3


Input

11
0.9
1
1
1.25
2.30000
5
70
0.000000001
9999.999999999
0.999999999
1.000000001


Output

8
"""

import collections

def count_integer_product_pairs(A):
    PRECISION_DIGITS = 9
    cnt = collections.defaultdict(int)
    
    for tmpA in A:
        tmpA = round(tmpA * 10 ** PRECISION_DIGITS)
        five = 0
        two = 0
        while tmpA % 2 == 0:
            two += 1
            tmpA //= 2
        while tmpA % 5 == 0:
            five += 1
            tmpA //= 5
        two -= PRECISION_DIGITS
        five -= PRECISION_DIGITS
        cnt[two, five] += 1
    
    ans = 0
    for (t1, cnt1) in cnt.items():
        for (t2, cnt2) in cnt.items():
            if 0 <= t1[0] + t2[0] and 0 <= t1[1] + t2[1]:
                if t1 < t2:
                    ans += int(cnt1 * cnt2)
                elif t1 == t2:
                    ans += int(cnt1 * (cnt2 - 1) / 2)
    
    return ans