"""
QUESTION:
For a given prime $\boldsymbol{p}$, define $\text{ord}_p(k)$ as the multiplicity of $\boldsymbol{p}$ in $\boldsymbol{\mbox{k}}$, i.e. the number of times $\boldsymbol{p}$ appears in the prime factorization of $\boldsymbol{k}$.

For a given $\boldsymbol{p}$ (prime) and $\boldsymbol{\mbox{L}}$, let $F(p,L)$ be the number of integers $n$ such that $1\leq n\leq L$ and $\text{ord}_p(n!)$ is divisible by $\boldsymbol{p}$. Here $n!$ denotes the factorial of $n$.

Your job is to calculate $F(p,L)$ given L$\boldsymbol{p}$ and $\boldsymbol{L}$.

Input Format 

The first line contains the number of test cases $\mathbf{T}$. 

Each of the next $\mathbf{T}$ lines contains two integers $\boldsymbol{p}$ and $\boldsymbol{\mbox{L}}$ separated by a space.

Output Format 

For each test case, output one line containing $F(p,L)$.

Constraints 

$1\leq T\leq1000000$ 

$2\leq p\leq10^{18}$ 

$1\leq L\leq10^{18}$ 

$\boldsymbol{p}$ is prime

Sample input  

2
2 6
3 6

Sample Output  

2
2

Explanation 

Here are the first 6 factorials: 1, 2, 6, 24, 120, 720.  

The multiplicities of 2 in these numbers are: 0, 1, 1, 3, 3, 4. 

Exactly two of these are divisible by 2 (0 and 4), so $F(2,6)=2$.

The multiplicities of 3 in these numbers are: 0, 0, 1, 1, 1, 2. 

Exactly two of these are divisible by 3 (0 and 0), so $F(3,6)=2$.
"""

def count_divisible_multiplicities(p: int, L: int) -> int:
    def ok(p, L):
        sum = 0
        while L > 0:
            sum += L % p
            L //= p
        return sum % p

    def solve(p, L):
        L1 = L // p
        r = p - ok(p, L1)
        if r == p:
            r = 0
        if r < L % p:
            return L1 + 1
        else:
            return L1

    L += 1
    L1 = L // p
    ans = 0
    if ok(p, L1) == 0:
        ans += L % p
    return ans + solve(p, L1) * p - 1