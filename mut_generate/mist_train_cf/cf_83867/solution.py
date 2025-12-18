"""
QUESTION:
Define a function `f(k, n)` that calculates the sum of `f_k(i)` for `i` ranging from `0` to `n`, where `f_k(i) = f_k(floor(i/k))`, `f_k(0) = 1`, and `floor(x)` represents the mathematical floor function. The function should take two parameters: `k` and `n`, where `k` is the base and `n` is the upper limit. The function should return the sum of `f_k(i)` for `i` ranging from `0` to `n`. 

Restrictions: The function should handle large inputs efficiently and should be able to calculate the result modulo `10^9 + 7`.
"""

MOD = 10**9+7

def f(k, n):
    if k == 1 or n <= 1:
        return (n*(n+1))//2
    else:
        return (f(k**2, n//k)*k + (n % k + 1)*(n//k + 1)//2) % MOD