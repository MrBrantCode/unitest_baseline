"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

The *beauty* of a sequence of non-negative integers is computed in the following way: for each of its non-empty (not necessarily contiguous) subsequences, compute the XOR of all elements of this subsequence; then, sum up all the XORs you obtained.

Let $F(N, B)$ denotes the number of non-negative integer sequences with length $N$ which have beauty $B$. You are given three integers $N$, $X$ and $M$. Find the smallest non-negative integer $B$ such that $F(N, B) \bmod M = X$, or determine that there is no such $B$. Since even the smallest such $B$ might be very large, compute its remainder modulo $998,244,353$.

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first and only line of each test case contains three space-separated integers $N$, $X$ and $M$.

------  Output ------
For each test case, print a single line containing one integer ― the smallest valid $B$ (modulo $998,244,353$), or $-1$ if there is no valid $B$.

------  Constraints  ------
$1 ≤ T ≤ 100$
$1 ≤ N ≤ 10^{10,000}$
$1 ≤ M ≤ 10^{9}$
$0 ≤ X < M$

------  Subtasks ------
Subtask #1 (45 points):
$N ≤ 10^{9}$
$M ≤ 10^{5}$

Subtask #2 (55 points): original constraints

----- Sample Input 1 ------ 
3

2 2 7

4 3 17

3 5 13
----- Sample Output 1 ------ 
6

-1

28
"""

from math import gcd, sqrt

modul = 998244353

def modiFun(a, b, p):
    a %= p
    b %= p
    if b == 1:
        return 0
    (count, t, g) = (0, 1, gcd(a, p))
    while g != 1:
        if b % g:
            return -1
        p = p // g
        b = b // g
        t = int(int(int(t * a) // g) % p)
        count += 1
        if b == t:
            return count
        g = gcd(a, p)
    (hash, base, m) = ({}, b, int(sqrt(1.0 * p) + 1))
    for i in range(m):
        hash[base] = i
        base = base * a % p
    (base, temp) = (pow(a, m, p), t)
    for i in range(1, m + 2):
        temp = temp * base % p
        if temp in hash.keys():
            return i * m - hash[temp] + count
    return -1

def find_smallest_beauty(n, x, m):
    if 1 % m == x:
        return 0
    if x == 0 and m == 1:
        return 0
    if x == 0 and n != 1:
        return 1
    
    var = (pow(2, n, m) - 1 + m) % m
    power = modiFun(var, x, m)
    
    if power == -1:
        return -1
    
    answ = pow(2, n - 1, modul) * (pow(2, power, modul) - 1 + modul) % modul % modul
    
    if answ == 0:
        if 1 % m != x:
            answ = -1
    if answ == 1:
        if 1 % m != x or n != -1:
            answ -= 1
    
    return answ