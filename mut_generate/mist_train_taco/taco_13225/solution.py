"""
QUESTION:
You are given an array $\mbox{A}$ of size $N$. You are asked to answer $\mbox{Q}$ queries.  

Each query contains a number $\mbox{M}$.  

For each distinct permutation of the array $\mbox{A}$, you need to print the sum of the values returned by the find function.

As the sum can be too large, output it modulo $\mbox{P}$, which is a prime and given in input.  

find(int permutation_A[], int M)
{
    x = Length(permutation_A)
    sum = 0
    for(i = 0; i < x; i++) {
        if (permutation_A[i] <= M)
            sum = sum + permutation_A[i]
        else
            break
    }
    return sum
}

Input Format 

The first line of input contains $\mbox{P}$. 

The second line of input contains $N$. The next line contains $N$ numbers $A[0]\ldots A[N-1]$ separated by single spaces. 

The next line contains $\mbox{Q}$, the number of queries to follow. Each subsequent line contains one positive integer $\mbox{M}$.  

Output Format 

For each query, output as asked above.  

Constraints 

$1000000\leq P\leq2000003$ 

$1\leq N\leq10^5$ 

$1\leq Q\leq10^5$ 

$1\leq A[i],M\leq10^9$

Sample Input

2000003
5
4 2 3 1 4
2
1
2

Sample Output

12
45

Explanation

Query 1: 

Consider all permutations. if the first number is greater than 1, then the loop will break in the beginning itself. There are a total of 60 distinct permutations out of which 48 will give 0. The remaining 12 will fetch 1 each from the function. Thus the answer is 12.
"""

from collections import defaultdict
from bisect import bisect_right

def calculate_sum_of_permutations(A, Q, queries, P):
    mod = P
    
    def binomial(n, k):
        if n < k or k < 0:
            return 0
        return fac[n] * invfac[k] * invfac[n - k] % mod

    def sum_(n, k):
        return (n * binomial(n + 1, k + 1) - binomial(n + 1, k + 2)) % mod

    def init(counter):
        n = len(counter)
        A = sorted(counter.keys())
        C = [counter[x] for x in A]
        N = sum(C)
        T = 0
        A_C = 0
        S = [0] * (n + 1)
        p = 1
        for c in C:
            p = p * invfac[c] % mod
        S[n] = p
        for i in range(1, n):
            T += C[i - 1]
            A_C += A[i - 1] * C[i - 1]
            S[i] = fac[N - T] * fac[T - 1] % mod
            S[i] = S[i] * A_C * p % mod
            S[i] = S[i] * ((N - 1) * binomial(N - 1, T - 1) - sum_(N - 2, N - 1 - T)) % mod
        A_C += A[n - 1] * C[n - 1]
        T += C[n - 1]
        S[n] = S[n] * fac[T] * A_C % mod
        return (S, A)

    N_max = 10 ** 5
    fac = [1] * (N_max + 1)
    invfac = [1] * (N_max + 1)
    for i in range(2, N_max + 1):
        fac[i] = fac[i - 1] * i % mod
    invfac[N_max] = pow(fac[N_max], mod - 2, mod)
    for i in reversed(range(2, N_max)):
        invfac[i] = invfac[i + 1] * (i + 1) % mod

    counter = defaultdict(int)
    for x in A:
        counter[x] += 1

    (S, A) = init(counter)

    results = []
    for M in queries:
        i = bisect_right(A, M)
        results.append(S[i])

    return results