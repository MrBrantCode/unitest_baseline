"""
QUESTION:
Write a function named `divide(N, M)` that takes two integers `N` and `M` as input, where 1 ≤ N ≤ 10^6 and 1 ≤ M ≤ 10^6. The function should perform the division of `N` by `M` using only bitwise operators, without using the division operator `/` or the modulo operator `%`, and return the quotient.
"""

def entrance(N, M):
    quotient = 0
    n = len(bin(N)) - 2
    m = len(bin(M)) - 2
    
    for i in range(n, m - 1, -1):
        shifted_divisor = M << (i - m)
        
        if N >= shifted_divisor:
            N -= shifted_divisor
            quotient |= (1 << (i - m))
            
    return quotient