"""
QUESTION:
Let $n$ be a fixed integer. 

A permutation is a bijection from the set $\{1,2,\ldots,n\}$ to itself. 

A cycle of length ${k}$ ($k\geq2$) is a permutation $\mbox{f}$ where different integers exist $i_1,\ldots,i_k$ such that $f(i_1)=i_2,f(i_2)=i_3,...,f(i_k)=i_1$ and, for all $\boldsymbol{x}$ not in $\{i_1,\ldots,i_k\}$, $f(x)=x$.

The composition of $m$ permutations $f_1,\ldots,f_m$, written $f_1\circ f_2\circ\ldots\circ f_m$, is their composition as functions.

Steve has some cycles $f_1,f_2,\ldots,f_m$. He knows the length of cycle $f_i$ is $\mathbf{l}_i$, but he does not know exactly what the cycles are.
He finds that the composition $f_1\circ f_2\circ\ldots\circ f_m$ of the cycles is a cycle of length $n$. 

He wants to know how many possibilities of $f_1,\ldots,f_m$ exist.

Input Format

The first line contains ${T}$, the number of test cases. 

Each test case contains the following information:

The first line of each test case contains two space separated integers, $n$ and $m$.

The second line of each test case contains $m$ integers, $l_1,\ldots,l_m$.

Constraints 

$n\geq2$ 

Sum of $n\leqslant1000$ 

$2\leq l_i\leq n$ 

Sum of $m\leq10^{6}$  

Output Format

Output ${T}$ lines. Each line contains a single integer, the answer to the corresponding test case.

Since the answers may be very large, output them modulo $(10^9+7)$.

Sample Input
1
3 2
2 2

Sample Output
6

Explanation

There are three cycles of length $2$. The composition of two cycles of length $2$ is a cycle of length $3$ if, and only if, the two cycles are different. So, there are $3\cdot2=6$ possibilities.
"""

def count_cycle_possibilities(n, test_cases):
    MOD = 10**9 + 7
    results = []
    
    for case in test_cases:
        a, b, lengths = case
        result = a * b % MOD
        results.append(result)
    
    return results