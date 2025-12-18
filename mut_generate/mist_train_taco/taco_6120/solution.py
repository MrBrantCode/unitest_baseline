"""
QUESTION:
Jzzhu has picked n apples from his big apple tree. All the apples are numbered from 1 to n. Now he wants to sell them to an apple store. 

Jzzhu will pack his apples into groups and then sell them. Each group must contain two apples, and the greatest common divisor of numbers of the apples in each group must be greater than 1. Of course, each apple can be part of at most one group.

Jzzhu wonders how to get the maximum possible number of groups. Can you help him?

Input

A single integer n (1 ≤ n ≤ 105), the number of the apples.

Output

The first line must contain a single integer m, representing the maximum number of groups he can get. Each of the next m lines must contain two integers — the numbers of apples in the current group.

If there are several optimal answers you can print any of them.

Examples

Input

6


Output

2
6 3
2 4


Input

9


Output

3
9 3
2 4
6 8


Input

2


Output

0
"""

import math

def maximize_apple_groups(n):
    if n <= 3:
        return 0, []
    
    halfpr = int(n / 2)

    def primes(n):
        primeslistsa = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317]
        yesnoprime = [False, False] + [True] * (n - 1)
        t = 0
        while primeslistsa[t + 1] <= int(math.sqrt(n)):
            t += 1
        for x in range(t + 1):
            for sa in range(2, int(n / primeslistsa[x] + 1)):
                yesnoprime[primeslistsa[x] * sa] = False
        return yesnoprime
    
    primeslist = primes(halfpr)
    totallist = [False] * (n + 1)
    applepairs = []
    
    for prime in range(len(primeslist) - 1, 1, -1):
        if primeslist[prime]:
            numprimes = int(n / prime)
            primesx = [int(i * prime) for i in range(1, numprimes + 1) if not totallist[i * prime]]
            if len(primesx) % 2 == 1:
                primesx.remove(2 * prime)
            for pr in primesx:
                applepairs.append(pr)
                totallist[pr] = True
    
    max_groups = int(len(applepairs) / 2)
    groups = [(applepairs[2 * t], applepairs[2 * t + 1]) for t in range(max_groups)]
    
    return max_groups, groups