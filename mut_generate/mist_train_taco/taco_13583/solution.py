"""
QUESTION:
Given are integers S and P.
Is there a pair of positive integers (N,M) such that N + M = S and N \times M = P?

-----Constraints-----
 - All values in input are integers.
 - 1 \leq S,P \leq 10^{12}

-----Input-----
Input is given from Standard Input in the following format:
S P

-----Output-----
If there is a pair of positive integers (N,M) such that N + M = S and N \times M = P, print Yes; otherwise, print No.

-----Sample Input-----
3 2

-----Sample Output-----
Yes

 - For example, we have N+M=3 and N \times M =2 for N=1,M=2.
"""

import math

def find_pair_for_sum_product(S: int, P: int) -> str:
    for i in range(1, math.floor(P ** 0.5) + 1):
        if P % i == 0 and P // i + i == S:
            return 'Yes'
    return 'No'