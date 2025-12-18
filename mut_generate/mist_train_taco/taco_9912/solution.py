"""
QUESTION:
You are given the equation $\tan\alpha=\frac{p}{q}$ and a positive integer, $n$. Calculate $\tan n\alpha$. There are $\mathbf{T}$ test cases.

Input Format

The first line contains $\mathbf{T}$, the number of test cases. 

The next $\mathbf{T}$ lines contain three space separated integers: $p,q$ and $n$, respectively.  

Constraints 

$0\leq p\leq10^9$ 

$1\leq q\leq10^9$ 

$1\leq n\leq10^9$ 

$T\leq10^4$

Output Format

If the result is defined, it is always a rational number. However, it can be very big. 

Output the answer modulo $(10^9+7)$. 

If the answer is $\frac{a}{b}$ and $\boldsymbol{b}$ is not divisible by $(10^9+7)$, there is a unique integer $0\leq x<10^9+7$ where $a\equiv bx\quad\text{mod}\:(10^9+7)$. 

Output this integer, $\boldsymbol{x}$. 

It is guaranteed that $\boldsymbol{b}$ is not divisible by $(10^9+7)$ for all test cases.  

Sample Input
2
2 1 2
5 6 7

Sample Output
666666670
237627959

Explanation

If $\tan\alpha=\frac{2}{1}$ then $\tan2\alpha=-\frac{4}{3}$ and 
$-4\equiv3\times666667670\mod(10^9+7)$. 

So, the answer is $\boldsymbol{66666670}$.
"""

def calculate_tan_n_alpha(p: int, q: int, n: int, P: int = 10**9 + 7) -> int:
    """
    Calculate tan(nα) modulo P given tan(α) = p/q.

    Parameters:
    p (int): Numerator of tan(α).
    q (int): Denominator of tan(α).
    n (int): The power of α.
    P (int): The modulo value (default is 10^9 + 7).

    Returns:
    int: The result of tan(nα) modulo P.
    """
    
    def mul(a, b):
        return ((a[0] * b[0] - a[1] * b[1]) % P, (a[0] * b[1] + a[1] * b[0]) % P)

    def my_pow(a, b):
        ret = (1, 0)
        while b > 0:
            if b & 1 == 1:
                ret = mul(ret, a)
            a = mul(a, a)
            b >>= 1
        return ret

    a = my_pow((q, p), n)
    return a[1] * pow(a[0], P - 2, P) % P