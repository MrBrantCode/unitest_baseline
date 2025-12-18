"""
QUESTION:
Kulyash loves perfect squares and hates perfect cubes.  
For any natural number N,  
F(N) = \texttt{number of perfect squares smaller than or equal to } N - \texttt{number of positive perfect cubes smaller than or equal to } N. 

Kulyash gives you an integer X and asks you to find the minimum value of N, such that F(N) ≥ X.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single line of input.
- The first and only line of each test case contains an integer X.

------ Output Format ------ 

For each test case, output on a new line, the minimum value of N such that F(N) ≥ X.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ X ≤ 10^{9}$

----- Sample Input 1 ------ 
3
1
3
3151

----- Sample Output 1 ------ 
4
25
11397376

----- explanation 1 ------ 
Test case $1$: There are $2$ perfect squares from $1$ to $4$, and $1$ perfect cube from $1$ to $4$, so $F(4) = 2 - 1 = 1$, as required. 

Test case $2$: There are $5$ perfect squares from $1$ to $25$, and $2$ perfect cubes from $1$ to $25$, so $F(25) = 5 - 2 = 3$, as required. 

Test case $3$: There are $3376$ perfect squares from $1$ to $11397376$, and $225$ perfect cubes from $1$ to $11397376$, so $F(11397376) = 3376 - 225 = 3151$, as required.
"""

import math

def find_min_N_for_F(X):
    start = X
    end = 10 ** 10
    mid = (start + end) // 2
    ans = 10 ** 20
    
    while start <= end:
        sq = mid
        zz = mid * mid
        cb = int(zz ** (1 / 3))
        val = cb + 1
        val = val ** 3
        if val == zz:
            cb += 1
        dif = sq - cb
        if dif >= X:
            ans = min(ans, zz)
            end = mid - 1
            mid = (start + end) // 2
        else:
            start = mid + 1
            mid = (start + end) // 2
    
    return ans