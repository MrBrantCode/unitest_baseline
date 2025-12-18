"""
QUESTION:
It is holi festival, festival of colors. Devu is having fun playing holi and is throwing balloons with his girlfriend Glynis. Police saw this mischief and tried arresting his girlfriend, Devu being a mathematician asked police not to arrest his girlfriend and instead torture him with brain teaser. Devu was a young engineering fellow and he did not knew that policeman was equally good in mathematics, policeman gave Devu a problem which is as follows:

Let $f(n,k)=n^k$

Your aim is to answer $f(n_1,k_1)^{f(n_2,k_2)}\:\text{mod}\:n$

Can you help devu and his girlfriend rescue from modern police.

Input Format

You are given ${T}$ which is the number of queries to solve.

Each Query consist of 5 space separated integers $n_{1},k_{1},n_{2},k_{2},n$

Constraints

$1\leq T\leq10^4$       
$0\leq n_1,k_1,n_2,k_2\leq10^9$       
$1\leq n\leq10^7$

Note The output to ${{0}^{{0}$ should be ${1}$. 

Output Format

Output contains exactly ${T}$ lines. $i^{\cdot th}$ line containing the answer for the $i^{\cdot th}$ query.

Sample Input
1
2 1 2 2 15

Sample Output
1

Explanation

$f(2,1)=2$

$f(2,2)=4$

so answer is $16\:\text{mod}\:15=1$
"""

def calculate_holi_queries(queries):
    lim = 3200
    mark = bytearray(lim)
    primes = [2]
    for i in range(3, lim, 2):
        if mark[i]:
            continue
        primes.append(i)
        for j in range(3 * i, lim, 2 * i):
            mark[j] = 1

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

    results = []
    for (n1, k1, n2, k2, n) in queries:
        if n1 == 0:
            f1 = 1 if k1 == 0 else 0
        else:
            f1 = pow(n1, k1, n) or n
        if n2 == 0:
            f2 = 1 if k2 == 0 else 0
        else:
            phi = 1
            for (p, e) in factor(n).items():
                phi *= (p - 1) * p ** (e - 1)
            f2 = pow(n2, k2, phi) or phi
        results.append(pow(f1, f2, n))
    
    return results