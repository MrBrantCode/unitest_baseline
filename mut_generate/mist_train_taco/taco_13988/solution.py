"""
QUESTION:
In mathematics, binomial coefficients are a family of positive integers that occur as coefficients in the binomial theorem.  
$\left(\begin{matrix}n\\ k\end{matrix}\right)$
denotes the number of ways of choosing k objects from n different objects.

However when n and k are too large, we often save them after modulo operation by a prime number P. Please calculate how many binomial coefficients of n become to 0 after modulo by P.

Input Format 

The first of input is an integer ${T}$, the number of test cases. 

Each of the following ${T}$ lines contains 2 integers, $n$ and prime ${P}$.  

Constraints 

$T<100$ 

$n<10^{500}$ 

$P<10^9$

Output Format

For each test case, output a line contains the number of   $\left(\begin{matrix}n\\ k\end{matrix}\right)$s (0<=k<=n)  each of which after modulo operation by P is 0.

Sample Input

3
2 2
3 2
4 3

Sample Output

1
0
1
"""

def count_zero_binomial_coefficients(n, p):
    a = []
    nn = n
    while nn > 0:
        a.append(nn % p)
        nn //= p
    m = 0
    for i in range(len(a)):
        b = a[-(i + 1)]
        m *= b + 1
        m += b
    return n - m