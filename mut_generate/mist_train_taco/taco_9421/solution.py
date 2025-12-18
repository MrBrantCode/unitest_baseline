"""
QUESTION:
For two positive integers a and b, let g(a, b) = [gcd]
(a, b) + [lcm](a, b). 

For a positive integer N, let f(N) denote the minimum value of g(a, b) over all the pairs of positive integers (a, b) such that a+b = N.

Find out the number of ordered pairs (a, b) such that a+b = N and g(a, b) = f(N). 

------ Input Format ------ 

- The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
- The first and only line of each test case contains a positive integer N.

------ Output Format ------ 

For each test case, output the number of ordered pairs (a, b) such that a+b = N and g(a, b) = f(N).

------ Constraints ------ 

$1 ≤ T ≤ 100$
$2 ≤ N ≤ 10^{9}$

----- Sample Input 1 ------ 
2
4
105
----- Sample Output 1 ------ 
3
14

----- explanation 1 ------ 
Test case $1$:
- For the pair $(1, 3)$, $g(1, 3) = gcd(1,3)+lcm(1,3)=1+3=4$.
- For the pair $(2, 2)$, $g(2, 2) = gcd(2,2)+lcm(2,2)=2+2=4$.
- For the pair $(3, 1)$, $g(3, 1) = gcd(3,1)+lcm(3,1)=1+3=4$.

Hence, $f(4) = 4$. There are three pairs $(a, b)$ satisfying $a+b = N$ and $g(a, b) = f(N)$.
"""

from math import gcd, sqrt

def g(a, b):
    return gcd(a, b) + (a * b) // gcd(a, b)

def f(N):
    min_g_value = float('inf')
    for a in range(1, N // 2 + 1):
        b = N - a
        current_g = g(a, b)
        if current_g < min_g_value:
            min_g_value = current_g
    return min_g_value

def snek(x):
    if x == 1:
        return 1
    ans = 2
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            ans += 1
            d = x // i
            if d != i:
                ans += 1
    return ans

def count_pairs_with_min_g(N):
    d = snek(N) - 1
    ans = 2 * d
    if N % 2 == 0:
        ans -= 1
    return ans