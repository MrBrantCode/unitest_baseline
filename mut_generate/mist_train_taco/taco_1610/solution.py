"""
QUESTION:
You're given three numbers: ${A}$, ${B}$, and $N$, and all you have to do is to find the number ${F}_N$ where 

$\begin{aligned}F_0&-A\\ F_1&=B\\ F_i&=F_{i-1}+F_{i-2}\:for\:i\geq2\end{aligned}$  

As the number can be very large, output it modulo $10^9+7$.  

Consider the following link: http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form

Input Format

First line contains a single integer ${T}$ - the number of tests.
${T}$ lines follow, each containing three integers: ${A}$, ${B}$ and $N$.

Constraints

$1\leq T\leq1000$ 

$1\leq A,B,N\leq10^9$  

Output Format

For each test case output a single integer $-$ ${F}_N$.  

Sample Input
8  
2 3 1  
9 1 7  
9 8 3  
2 4 9  
1 7 2  
1 8 1  
4 3 1  
3 7 5  

Sample Output
3  
85  
25  
178  
8  
8  
3  
44

Explanation

First test case is obvious. 

Let's look through the second one: 

$F_{0}=9$ 

$F_1=1$ 

$F_2=1+9=10$ 

$F_3=10+1=11$ 

$F_4=11+10=21$ 

$F_5=21+11=32$ 

$F_6=32+21=53$ 

$F_7=53+32=85$
"""

MOD = 1000000007

def mul(A, B):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for h in range(2):
                res[i][j] = (res[i][j] + A[i][h] * B[h][j]) % MOD
    return res

def compute_fibonacci_mod(a, b, n):
    res = [[1, 0], [0, 1]]
    x = [[0, 1], [1, 1]]
    while n:
        if n % 2 == 1:
            res = mul(res, x)
        x = mul(x, x)
        n //= 2
    return (res[0][0] * a + res[0][1] * b) % MOD