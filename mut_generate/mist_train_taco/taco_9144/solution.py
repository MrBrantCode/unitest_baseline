"""
QUESTION:
You have 4 bags A, B, C and D each of which includes N coins (there are totally 4N coins). Values of the coins in each bag are ai, bi, ci and di respectively.

Find the number of combinations that result when you choose one coin from each bag (totally 4 coins) in such a way that the total value of the coins is V. You should distinguish the coins in a bag.

Constraints

* 1 ≤ N ≤ 1000
* 1 ≤ ai, bi, ci, di ≤ 1016
* 1 ≤ V ≤ 1016
* All input values are given in integers

Input

The input is given in the following format.


N V
a1 a2 ... aN
b1 b2 ... bN
c1 c2 ... cN
d1 d2 ... dN


Output

Print the number of combinations in a line.

Examples

Input

3 14
3 1 2
4 8 2
1 2 3
7 3 2


Output

9


Input

5 4
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1


Output

625
"""

from collections import defaultdict

def count_coin_combinations(N, V, a, b, c, d):
    mp = defaultdict(int)
    
    # Precompute the sums of coins from bags C and D
    for val1 in c:
        for val2 in d:
            mp[val1 + val2] += 1
    
    # Count the valid combinations from bags A and B
    ans = 0
    for val1 in a:
        for val2 in b:
            ans += mp[V - val1 - val2]
    
    return ans