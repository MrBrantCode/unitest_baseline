"""
QUESTION:
Write a function `G(N, mod=1000000007)` that calculates the sum of the maximum quantity of paper that can be conserved by wrapping `n` identical cubes in a compact configuration for all `n` from 1 to `N`, modulo `mod`. The function should return the result modulo `1,000,000,007`.
"""

def G(N, mod=1000000007):
    maxsaved = [0]*(N+1)
    for i in range(1, N+1):
        for j in range(1, int(i**0.5)+1):
            if i%j==0:
                for k in range(j, int(i/j)+1):
                    l = i//(j*k)
                    papersaved = 2*i - 2*(j*k + k*l + l*j)
                    maxsaved[i] = max(maxsaved[i], papersaved)
                    
    return sum(maxsaved) % mod