"""
QUESTION:
After Derek (of district 5) discovered how to compute the greatest common divisor (gcd) of Fibonacci numbers, he now tried to answer the next obvious question: how does one compute the least common multiple (lcm) of Fibonacci numbers? Unfortunately, Derek found out that this wasn't as easy as the original problem, so he asked you to answer it for him.

The Fibonacci numbers are defined as:

$F_1=F_2=1$
$F_n=F_{n-1}+F_{n-2}$

Given $N$ integers $a_1,a_2,\ldots,a_N$, find $\text{lcm}(F_{a_1},F_{a_2},\ldots,F_{a_N})$, and give your answer modulo $10^9+7$.

Input Format 

The first line of input contains $N$. 

Each of the next $N$ lines contains a number: the $i^{th}$ line contains $a_i$.

Constraints 

$1\leq N\leq100$ 

$1\leq a_i\leq10^9$  

Output Format 

Print a single integer, which is the least common multiple of the ${F}_{a_i}$, modulo $10^9+7$.

Sample Input  

5
1
3
3
6
9

Sample Output  

136

Explanation 

$\text{lcm}(F_1,F_3,F_3,F_6,F_9)=\text{lcm}(1,2,2,8,34)=136$
"""

import sys
from math import gcd

def fib_mod(n, mod):
    if n <= 2:
        return ((n + 1 >> 1) % mod, (n + 2 >> 1) % mod)
    mask = 4
    while mask <= n:
        mask <<= 1
    mask >>= 2
    (a, b) = (1, 1)
    while mask:
        if mask & n:
            (a, b) = ((a * a + b * b) % mod, b * ((a << 1) + b) % mod)
        else:
            (a, b) = (a * ((b << 1) - a) % mod, (a * a + b * b) % mod)
        mask >>= 1
    return (a, b)

def compute_lcm_of_fibonacci(N, indices, MOD=10**9 + 7):
    def solve(seq):
        seq = sorted(seq)
        next = []
        for i in range(len(seq)):
            for j in range(i + 1, len(seq)):
                if seq[j] % seq[i] == 0:
                    break
            else:
                next.append(seq[i])
        seq = next[:]
        ans = 1
        for i in range(len(seq)):
            c = seq[i]
            ans = ans * fib_mod(c, MOD)[0] % MOD
            t = 1
            s = set()
            for g in seq[:i]:
                s.add(gcd(g, c))
            s = list(sorted(s))
            k = solve(s)
            ans = ans * pow(k, MOD - 2, MOD) % MOD
        return ans
    
    return solve(indices)