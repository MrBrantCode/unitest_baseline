"""
QUESTION:
You are given positive integers $L$ and $R$. You have to find the sum
S=∑i=LR(L∧(L+1)∧…∧i),S=∑i=LR(L∧(L+1)∧…∧i),S = \sum_{i=L}^R \left(L \wedge (L+1) \wedge \ldots \wedge i\right) \,,
where $\wedge$ denotes the bitwise AND operation. Since the sum could be large, compute it modulo $10^9+7$.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $L$ and $R$.

-----Output-----
For each test case, print a single line containing one integer — the sum $S$ modulo $10^9+7$.

-----Constraints-----
- $1 \le T \le 10^5$
- $1 \le L \le R \le 10^{18}$

-----Example Input-----
2
1 4
4 10

-----Example Output-----
1
16

-----Explanation-----
Example case 1: The sum is 1 + 1 AND 2 + 1 AND 2 AND 3 + 1 AND 2 AND 3 AND 4 = 1 + 0 + 0 + 0 = 1.
Example case 2: The sum is 4 + 4 AND 5 + 4 AND 5 AND 6 + 4 AND 5 AND 6 AND 7 + … + 4 AND 5 AND … AND 10 = 4 + 4 + … + 0 = 16.
"""

import math

def calculate_bitwise_and_sum(L, R):
    power = int(math.log(L, 2))
    add = 0
    mod = 10 ** 9 + 7
    previous_i = -1
    present = 0
    end = 0
    for i in range(power + 1):
        bit_add = 2 ** i
        end += 2 ** i
        if L & bit_add == bit_add:
            present += bit_add
            total_added = min(R - L + 1, end - present + 1)
            add += bit_add * total_added
    return add % mod