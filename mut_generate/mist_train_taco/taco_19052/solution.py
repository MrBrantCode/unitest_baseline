"""
QUESTION:
You are given an integer N. 

You are asked to find total number of integer pairs (A,B) such that
1 ≤ A,B ≤ N
A^{2}+B^{2}+gcd^{2}(A,B)+lcm^{2}(A,B)=N. Note that gcd^{2}(A, B) and lcm^{2}(A, B) denote the square of [gcd] and the square of [lcm] of numbers A and B respectively.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- The only line of each test case contains an integer N.

------ Output Format ------ 

For each test case, output in a single line, number of valid pairs (A,B).

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$4 ≤ N ≤ 10^{10}$
- Sum of $N$ over all test cases does not exceed $10^{10}$.

----- Sample Input 1 ------ 
3
4
10
20

----- Sample Output 1 ------ 
1
2
2

----- explanation 1 ------ 
Test case 1: The only valid pair is $(1, 1)$. Here:
- $1≤ 1 ≤ 4$.
- $1^{2} + 1^{2} + gcd^{2}(1,1) + lcm^{2}(1,1) = 1+1+1+1=4$.

Test case 2: Only $2$ pairs are possible. These are: $(1, 2)$ and $(2, 1)$.
- For pair $(1, 2)$: $1≤ 1, 2≤ 10$ and $1^{2}+2^{2}+gcd^{2}(1,2)+lcm^{2}(1,2)=1+4+1+4=10$. 

Test case 3: Only $2$ pairs are possible. These are: $(1, 3)$ and $(3, 1)$.
- For pair $(1, 3)$: $1≤ 1, 3≤ 20$ and $1^{2}+3^{2}+gcd^{2}(1,3)+lcm^{2}(1,3)=1+9+1+9=20$.
"""

import itertools
import math

def factorize(n):
    def try_divisor(n, k, pfs):
        if n % k == 0:
            pfs[k] = 1
            n //= k
            while n % k == 0:
                pfs[k] += 1
                n //= k
        return n
    
    pfs = {}
    n = try_divisor(n, 2, pfs)
    n = try_divisor(n, 3, pfs)
    for i in itertools.count(start=1):
        n = try_divisor(n, 6 * i - 1, pfs)
        n = try_divisor(n, 6 * i + 1, pfs)
        if (6 * i + 1) ** 2 > n:
            break
    if n > 1:
        pfs[n] = 1
    return pfs

def recurse(lpfs, i, aa, bb):
    if i == len(lpfs):
        a = math.isqrt(aa - 1)
        b = math.isqrt(bb - 1)
        if a > 0 and b > 0 and (a * a + 1 == aa) and (b * b + 1 == bb) and (math.gcd(a, b) == 1):
            return 1
        else:
            return 0
    (p, e) = lpfs[i]
    if p == 2:
        if e % 2 == 1:
            return recurse(lpfs, i + 1, 2 * aa, bb) + recurse(lpfs, i + 1, aa, 2 * bb)
        else:
            return recurse(lpfs, i + 1, aa, bb) + recurse(lpfs, i + 1, 2 * aa, 2 * bb)
    else:
        return sum((recurse(lpfs, i + 1, aa * p ** j, bb * p ** k) for j in range(e + 1) for k in range(e - j + 1) if (e - j - k) % 2 == 0))

def count_valid_pairs(N):
    pfs = factorize(N)
    ok = True
    lpfs = []
    while pfs:
        (p, e) = pfs.popitem()
        if p % 4 == 3:
            if e % 2 == 1:
                ok = False
                break
        else:
            lpfs.append((p, e))
    return recurse(lpfs, 0, 1, 1) if ok else 0