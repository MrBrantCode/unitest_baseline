"""
QUESTION:
You are given an integer N. Find the number of distinct XORs it is possible to make using two positive integers no larger than N.

Formally, let S be the set
S = \{x\oplus y \mid 1 ≤ x, y ≤ N\}

where \oplus denotes the [bitwise XOR] operation. 

Find |S| (where |S| denotes the size of set S. Note that a set, by definition, has no repeated elements). The answer might be large, so output it modulo 10^{9} + 7.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of a single line of input, which contains one integer N.

------ Output Format ------ 

For each test case, output a single line containing the answer, modulo 10^{9} + 7.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{12}$

----- Sample Input 1 ------ 
3
1
3
7
----- Sample Output 1 ------ 
1
4
8
----- explanation 1 ------ 
Test Case 1: $N = 1$, so the only XOR we can possibly make is $1 \oplus 1 = 0$. Thus, the answer is $1$.

Test Case 2: $N = 3$, which gives us $S = \{0, 1, 2, 3\}$ as the set of possible XORs. Thus, the answer is $|S| = 4$.
"""

import math

def count_distinct_xors(N: int) -> int:
    MOD = 1000000007
    
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif (N & (N - 1)) == 0:
        return ((N * 2 - 1) % MOD)
    else:
        a = math.floor(math.log(N, 2))
        n = 2 ** (a + 1)
        return (n % MOD)