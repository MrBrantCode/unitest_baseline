"""
QUESTION:
Tara has an array, $\mbox{A}$, consisting of $n$ integers where each integer occurs at most $2$ times in the array. 

Let's define $\mbox{P}$ to be a permutation of $\mbox{A}$ where $p_i$ is the $i^{\mbox{th}}$ element of permutation $\mbox{P}$. Tara thinks a permutation is beautiful if there is no index $\boldsymbol{i}$ such that $p_{i}-p_{i+1}=0$ where $i\in[0,n-1)$.

You are given $\textit{q}$ queries where each query consists of some array $\mbox{A}$. For each $\mbox{A}$, help Tara count the number of possible beautiful permutations of the $n$ integers in $\mbox{A}$ and print the count, modulo $10^9+7$, on a new line.

Note: Two permutations, $\mbox{P}$ and $\mbox{Q}$, are considered to be different if and only if there exists an index $\boldsymbol{i}$ such that $p_i\neq q_i$ and $i\in[0,n)$.

Input Format

The first line contains a single integer, $\textit{q}$, denoting the number of queries. The $2\cdot q$ subsequent lines describe each query in the following form:

The first line contains an integer, $n$, denoting the number of elements in array $\mbox{A}$. 
The second line contains $n$ space-separated integers describing the respective values of $a_0,a_1,\ldots,a_{n-1}$ in array $\mbox{A}$.

Constraints

$1\leq a_i\leq10^9$
Each integer in $\mbox{A}$ can occur at most $2$ times.

For $\textbf{40\%}$ of the maximum score:

$1\leq q\leq100$    
$1\leq n\leq1000$  
The sum of $n$ over all queries does not exceed $\mathbf{10}^4$.  

For $\textbf{100\%}$ of the maximum score:  

$1\leq q\leq100$    
$1\leq n\leq2000$

Output Format

For each query, print the the number of possible beautiful permutations, modulo $10^9+7$, on a new line.

Sample Input 0
3
3
1 1 2
2
1 2
4
1 2 2 1

Sample Output 0
1
2
2

Explanation 0

We perform the following $q=3$ queries:

Array $A=[1,2,1]$ and there is only one good permutation: 

Thus, we print the result of $1\:\text{mod}\:(10^9+7)=1$ on a new line.

Array $A=[1,2]$ and there are two good permutations: 

Thus, we print the result of $2\ \text{mod}\ (10^9+7)=2$ on a new line.

Array $A=[1,2,2,1]$ and there are two good permutations: 

For demonstration purposes, the following two permutations are invalid (i.e., not good): 

Because we only want the number of good permutations, we print the result of $2\ \text{mod}\ (10^9+7)=2$ on a new line.
"""

def count_beautiful_permutations(A: list) -> int:
    """
    Counts the number of beautiful permutations of the array A modulo 10^9 + 7.

    A beautiful permutation is defined as a permutation where no two adjacent elements are the same.

    Parameters:
    A (list): The input array of integers where each integer occurs at most twice.

    Returns:
    int: The number of beautiful permutations modulo 10^9 + 7.
    """
    MOD = 1000000007
    INV2 = (MOD + 1) // 2
    _factorials = {}

    def factorial(x):
        if x in {0, 1}:
            return 1
        if x in _factorials:
            return _factorials[x]
        retv = x * factorial(x - 1) % MOD
        _factorials[x] = retv
        return retv

    _bin = {}

    def binomial(n, k):
        if k == n or k == 0:
            return 1
        if k < 0 or k > n:
            return 0
        if (n, k) in _bin:
            return _bin[n, k]
        retv = (binomial(n - 1, k) + binomial(n - 1, k - 1)) % MOD
        _bin[n, k] = retv
        return retv

    mults = {}
    for x in A:
        mults[x] = mults.get(x, 0) + 1
    npairs = sum((1 for v in mults.values() if v == 2))
    nsingles = sum((1 for v in mults.values() if v == 1))
    ntot = len(A)
    retv = 0
    twoinvpow = 1
    for i in range(npairs + 1):
        cp = npairs - i
        v = factorial(ntot - cp) * twoinvpow * binomial(npairs, cp)
        twoinvpow = twoinvpow * INV2 % MOD
        retv += v if cp % 2 == 0 else MOD - v
    return retv % MOD