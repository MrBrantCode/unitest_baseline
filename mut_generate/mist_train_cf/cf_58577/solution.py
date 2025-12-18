"""
QUESTION:
Write a function LC(m, n, mod) that calculates the total number of valid assignments of numbers for L(m, n) modulo mod, where L(m, n) is an m x m grid from which the top-right n x n grid has been excised. The number in every cell should be less than the number in the cell directly below it and to its immediate left. The function should be able to handle large inputs and should return the result modulo mod.
"""

def entrance(m, n, mod):
    factorial = [0] * ((m << 1) + 1)
    inverse = [0] * ((m << 1) + 1)
    factorial[0] = factorial[1] = inverse[0] = inverse[1] = 1
    
    for i in range(2, (m << 1) + 1):
        factorial[i] = (factorial[i - 1] * i) % mod
        inverse[i] = (inverse[mod % i] * (mod - mod // i)) % mod

    for i in range(2, (m << 1) + 1):
        inverse[i] = (inverse[i - 1] * inverse[i]) % mod
    
    def comb(n, k):
        if n < k or k < 0: 
            return 0
        return (factorial[n] * inverse[k] % mod) * inverse[n - k] % mod      
    return (comb(m << 1, m) - comb(m << 1, m - n - 1) + mod) % mod