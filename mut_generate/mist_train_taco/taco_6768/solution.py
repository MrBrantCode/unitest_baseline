"""
QUESTION:
Ichigo is on his way to save Rukia. Unfortunately, when Ichigo was busy fighting Renji, Kenpachi Zaraki had gone to the Dangai(the same place where Ichigo got his final Getsuga Tenshou) to train. Now, he has a Bankai called Tensa Quantum Computer and he used it against Ichigo!

Tensa Quantum Computer consists of 2N rooms arranged in a circle. Kenpachi imprisoned Rukia in one of these rooms. The rooms have the numbers 1, 2, ..., N-1, N, -N, -(N-1), ..., -1 written on them in that order clockwise. Each room has a one-way door to another unique room. Kenpachi knows that if a room has number X, then it leads to another room which is at distance abs(X) from this room. More precisely, if X is positive, it means that this room leads to the X-th room in the clockwise direction from the current room. And if X is negative, then that means that this room leads to the (-X)-th room in the anticlockwise direction from the current room.

Kenpachi knows that Ichigo starts at the room with the number A. Being a determined guy, Ichigo doesn't sit still until he finds Rukia. Instead he keeps running to the next room for as long as he can. But Kenpachi's funny and crafty lieutenant Yachiru Kusajishi suggested that if Kenpachi keeps Rukia in one of the rooms that Ichigo will never visit, then Ichigo will keep running forever and die from exhaustion.

Now, Kenpachi wants to know the number of rooms that he can keep Rukia in, so that poor Ichigo never finds her and hence, keeps running.

Note: abs(X) is the absolute value of X.

Input Format

Line 1: T 

T - Number of test cases. 

Lines 2 to T+1: N A 

N - Half the total number of rooms. 

A - The number of the room where Ichigo starts his pursuit of Rukia.  

Output Format

For each test case, print a single integer in a new line that is the number of rooms where Kenpachi can imprison Rukia so that Ichigo never finds her.

Constraints

1 <= T <= 1000 

1 <= N <= 10^{9} 

1 <= abs(A) <= N

Sample Input

4
1 1
4 1
4 -3
1729 -786

Sample Output

0
2
6
3170

Explanation

In the first test case, the rooms that Ichigo visits have numbers 1, -1, 1, -1, ... in that order. So, there are no unvisited rooms. 

In the second test case, the rooms that Ichigo visits have numbers 1, 2, 4, -1, -2, -4, 1, 2, ... in that order. So, there are two unvisited rooms namely the ones numbered 3 and -3. 

In the third test case, the rooms that Ichigo visits have numbers -3, 3, -3, 3, ... in that order. So, there are six unvisited rooms namely the ones numbered 1, 2, 4, -4, -2, -1.
"""

import math

def sieve(lim):
    primes = [2]
    mark = bytearray(lim)
    for i in range(3, lim, 2):
        if mark[i]:
            continue
        primes.append(i)
        for j in range(3 * i, lim, 2 * i):
            mark[j] = 1
    return primes

primes = sieve(45000)

def factor(n):
    f = {}
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            n //= p
            f[p] = f.get(p, 0) + 1
    if n > 1:
        f[n] = 1
    return f

def totient(n):
    f = factor(n)
    t = 1
    for p in f:
        t *= (p - 1) * p ** (f[p] - 1)
    return t

def count_unreachable_rooms(T, test_cases):
    results = []
    for t in range(T):
        N, A = test_cases[t]
        m = 2 * N + 1
        m //= math.gcd(m, A % m)
        t = totient(m)
        for p in factor(t):
            while t % p == 0 and pow(2, t // p, m) == 1:
                t //= p
        results.append(2 * N - t)
    return results