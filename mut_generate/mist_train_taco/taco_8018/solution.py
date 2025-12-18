"""
QUESTION:
You are given two integers $N$ and ${L}}$. Compute the number of unrooted labelled trees with exactly $N$ nodes and exactly ${L}$ leafs. This number can be huge, so please output it's modulo $10^9+7$.

Input Format

The first line of input consists of two space separated integers $N$ and ${L}$.

Constraints

$1\leq L<N\leq10^{6}$

Output Format

Display an answer to the problem on first line of the output.

Sample Input
5 2
Sample Output

60
"""

def count_unrooted_labelled_trees(n, l, P=10**9 + 7):
    if n == 2:
        return 1 if l == 0 else 0

    def C(n, k):
        return fact[n] * inv_fact[k] % P * inv_fact[n - k] % P
    
    fact = [1]
    for i in range(1, n + 1):
        fact.append(fact[-1] * i % P)
    
    inv = [0, 1]
    for i in range(2, n + 1):
        inv.append(P - P // i * inv[P % i] % P)
    
    inv_fact = [1]
    for i in range(1, n + 1):
        inv_fact.append(inv_fact[-1] * inv[i] % P)
    
    k = n - l
    ret = 0
    for used in range(1, k + 1):
        delta = C(k, used) * pow(used, n - 2, P) % P
        if used & 1 == k & 1:
            ret += delta
        else:
            ret -= delta
    
    return ret % P * C(n, k) % P