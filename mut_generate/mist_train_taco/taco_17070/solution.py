"""
QUESTION:
------Read problems statements in Hindi,
Mandarin chinese
, Russian and Vietnamese as well. ------ 

At ShareChat, there are are plenty of interesting problems to solve. Here is one of them.

Given integers $A$, $B$ and $N$, you should calculate the [GCD] of $A^{N} + B^{N}$ and $|A - B|$. (Assume that $GCD(0, a) = a$ for any positive integer $a$). Since this number could be very large, compute it modulo $1000000007$ ($10^{9} + 7$).

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains three space-separated integers $A$, $B$ and $N$.

------  Output ------
For each test case, print a single line containing one integer — the required GCD modulo $10^{9} + 7$.

------  Constraints ------
$1 ≤ T ≤ 10$
$1 ≤ A, B, N ≤ 10^{12}$
$B ≤ A$

------  Subtasks ------
Subtask #1 (10 points): $1 ≤ A, B, N ≤ 10$

Subtask #2 (40 points): $1 ≤ A, B, N ≤ 10^{9}$

Subtask #3 (50 points): original constraints

----- Sample Input 1 ------ 
2
10 1 1
9 1 5
----- Sample Output 1 ------ 
1
2
----- explanation 1 ------ 
Example case 1: $GCD(10^{1} + 1^{1}, 10 - 1) = GCD(11, 9) = 1$

Example case 2: $GCD(9^{5} + 1^{5}, 9 - 1) = GCD(59050, 8) = 2$
"""

import math

def power(a, n, mod):
    res = 1
    while n > 0:
        if n & 1 == 1:
            res = res % mod * a % mod % mod
            n -= 1
        a = a % mod * a % mod % mod
        n = n // 2
    return res

def calculate_gcd_modulo(A, B, N, mod=1000000007):
    if A == B:
        return (power(A, N, mod) + power(B, N, mod)) % mod
    possible = 1
    total = A - B
    for i in range(1, int(math.sqrt(total)) + 1):
        if total % i == 0:
            temp = (power(A, N, i) + power(B, N, i)) % i
            if temp == 0:
                possible = max(possible, i)
            temp = (power(A, N, total // i) + power(B, N, total // i)) % (total // i)
            if temp == 0:
                possible = max(possible, total // i)
    return possible % mod