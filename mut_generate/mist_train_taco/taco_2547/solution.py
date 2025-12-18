"""
QUESTION:
Takahashi has N balls with positive integers written on them. The integer written on the i-th ball is A_i. He would like to form some number of pairs such that the sum of the integers written on each pair of balls is a power of 2. Note that a ball cannot belong to multiple pairs. Find the maximum possible number of pairs that can be formed.

Here, a positive integer is said to be a power of 2 when it can be written as 2^t using some non-negative integer t.

Constraints

* 1 \leq N \leq 2\times 10^5
* 1 \leq A_i \leq 10^9
* A_i is an integer.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Print the maximum possible number of pairs such that the sum of the integers written on each pair of balls is a power of 2.

Examples

Input

3
1 2 3


Output

1


Input

5
3 11 14 5 13


Output

2
"""

from collections import Counter

def max_pairs_with_power_of_2_sum(N, A):
    cnt = Counter(A)
    A.sort(reverse=True)
    Ps = [2]
    for i in range(29):
        Ps.append(Ps[-1] * 2)
    
    ans = 0
    for A_i in A:
        if cnt[A_i] <= 0:
            continue
        cnt[A_i] -= 1
        while Ps[-1] > 2 * A_i:
            Ps.pop()
        if cnt[Ps[-1] - A_i] > 0:
            ans += 1
            cnt[Ps[-1] - A_i] -= 1
    
    return ans