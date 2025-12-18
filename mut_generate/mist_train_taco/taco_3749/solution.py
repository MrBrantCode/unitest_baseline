"""
QUESTION:
Manasa is a student in the department of Mathematics. She is pretty good at doing calculations involving small numbers, but large numbers scare her. So she wants you to help her in the following calculations.

Given two numbers in the following manner:

$A=p_1^{a_1}\times p_2^{a_2}\times p_3^{a_3}\times\text{...}\times p_N^{a_N}$
$B=p_1^{b_1}\times p_2^{b_2}\times p_3^{b_3}\times\text{...}\times p_N^{b_N}$

($p_i$ is a prime number, and all the $p_i$'s are distinct)

She wants you to calculate ${S}$ for her, where ${S}$ is the sum of $m+n$ for all pairs of numbers  where $m\leq n$, $\text{gcd}(m,n)=B$ and $\text{lcm}(m,n)=A$. In other words:

$S=\sum_{\begin{equation}\begin{aligned}gcd(m,n)=B\\ \text{lcm}(m,n)=A\\ m\leq n}}(m+n)$ 

As the value of ${S}$ can be very large, she wants you to print $S\:\text{mod}\:10^9+7$.

Input Format 

The first line contains an integer $N$, the number of prime factors. 

Each of the next $N$ lines contains three numbers: $p_i$, $b_i$ and $a_i$.

Output Format 

Print the value of $S\:\text{mod}\:10^9+7$.

Constraints  

$1\leq N\leq500$ 

$2\leq p_i\leq5000$ 

$1\leq a_i\leq10^9$ 

$1\leq b_i\leq10^9$ 

$b_i\leq a_i$  

Sample Input

2
2 1 2 
3 1 2

Sample Output

72

Explanation

We have $B=6$ and $A=36$. There are two pairs of integers $(m,n)$ with ${gcd}$ equal to ${6}$ and ${lcm}$ equal to $36$, and such that $m\leq n$. These are $(12,18)$ and $(6,36)$:

$\text{gcd}(12,18)=6$ and $\text{lcm}(12,18)=36$  
$\text{gcd}(6,36)=6$ and $\text{lcm}(6,36)=36$  

Hence, $S=(12+18)+(6+36)=72$
"""

def calculate_sum_S(N, data):
    P = 10 ** 9 + 7
    ret = 1
    allEq = True
    
    for (p, a, b) in data:
        if a == b:
            ret *= pow(p, a, P)
        else:
            allEq = False
            ret *= (pow(p, a, P) + pow(p, b, P)) % P
        ret %= P
    
    if allEq:
        ret = ret * 2 % P
    
    return ret