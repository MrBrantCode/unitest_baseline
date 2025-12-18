"""
QUESTION:
Write a function G(N) to compute the value of $G(N)=\sum_{j=1}^N\sum_{i=1}^j \gcd(i,j)$, and return the result modulo $998244353$. The function should be efficient enough to handle large values of N, such as $N=10^{11}$.
"""

def phi(N): 
    result = N   
    p = 2   
    while(p * p <= N): 
        if (N % p == 0): 
            while (N % p == 0): 
                N //= p 
            result -= result // p 
        p += 1
    if (N > 1): 
        result -= result // N 
    return result 

MOD=998244353

def G(N): 
    result = 0 
    for d in range(1,N+1): 
        for k in range(1,N//d+1): 
            result = (result + k * phi(k) * d) % MOD 
    return result 