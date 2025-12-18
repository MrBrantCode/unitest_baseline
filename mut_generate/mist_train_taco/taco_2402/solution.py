"""
QUESTION:
Given two integers A and B, find the count of integers X \in [L, R] such that at least one of the following is true:
X and A are [coprime]
X and B are [coprime]

------ Input Format ------ 

- The first and only line of input contains four integers A,B,L, and R: as given in the problem statement.

------ Output Format ------ 

- Print a single integer denoting the count of integers X satisfying the condition.

------ Constraints ------ 

$1 ≤ A,B ≤ 10^{9}$
$1 ≤ L ≤ R ≤ 10^{18}$

----- Sample Input 1 ------ 
6 15 1 10

----- Sample Output 1 ------ 
6

----- explanation 1 ------ 
There are $6$ numbers that satisfy the condition: $1,2,4,5,7,8$.

----- Sample Input 2 ------ 
235714494 193478285 2 100000000000

----- Sample Output 2 ------ 
65435081000

----- explanation 2 ------
"""

def count_coprime_integers(A, B, L, R):
    possible_pfs = [2, 3] + [6 * x + d for x in range(1, 5271) for d in [-1, 1]]

    def ceilq(a, b):
        return (a + b - 1) // b

    def prime_factors(n):
        pfs = set({})
        for p in possible_pfs:
            if n % p == 0:
                pfs.add(p)
                while n % p == 0:
                    n //= p
            if p * p > n:
                break
        if n > 1:
            pfs.add(n)
        return pfs

    def copr(l, r, x):
        if x:
            y = x.copy()
            p = y.pop()
            return copr(l, r, y) - copr(ceilq(l, p), r // p, y)
        else:
            return r - l + 1

    pfs_a = prime_factors(A)
    pfs_b = prime_factors(B)
    pfs_ab = pfs_a | pfs_b
    
    return copr(L, R, pfs_a) + copr(L, R, pfs_b) - copr(L, R, pfs_ab)