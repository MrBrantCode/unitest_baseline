"""
QUESTION:
You are given an integer $N$. Consider set $S=\{0,\:1,\ldots,\:2^N-1\}$. How many subsets $A\subset S$ with $\bigoplus_{x\in A}x=0$ ($\theta$ denotes xor operation) are there? 

Print your answer modulo $(10^9+7)$. 

Note that the  xorsum of an empty set is zero!  

Input Format 

The first line contains one integer $\mathbf{T}$, the number of testcases. 

The next $\mathbf{T}$ lines contain one integer $N$ each.

Output Format 

Output $\mathbf{T}$ lines. Each line is one number, answer to the problem modulo $10^9+7$.

Constraints 

$1\leq T\leq10000$ 

$1\leq N\leq10^{18}$

Sample Input  

2
1
2

Sample Output  

2
4

Explanation 

For $N=1$ there are $2$ sets - ∅ and $\{0\}$. 

For $N=2$ there are $4$ sets - ∅, $\{0\}$, $\{1,\:2,\:3\}$, $\{0,\:1,\:2,\:3\}$.
"""

def count_xor_zero_subsets(N: int) -> int:
    MOD = 10 ** 9 + 7
    ex = (pow(2, N, MOD - 1) - N) % (MOD - 1)
    return pow(2, ex, MOD)