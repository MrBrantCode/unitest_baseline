"""
QUESTION:
Calculate the total number of permutations from 1 to `n` such that prime numbers are positioned at prime indices (1-indexed), with the result returned modulo `10^9 + 7`. A number is considered prime if it exceeds 1 and cannot be expressed as a product of two positive integers less than it. The function name is `numPrimeArrangements`. The input `n` satisfies the constraint `1 <= n <= 100`.
"""

def numPrimeArrangements(n):
    mod = 10 ** 9 + 7

    def factorial(n):
        f = [1] * (n+1)
        for i in range(2, n+1):
            f[i] = f[i-1] * i % mod
        return f

    primecount = [0,0,1,2,2,3,3,4,4,4,4]
    if n < 10: 
        return factorial(n)[primecount[n]] * factorial(n)[n - primecount[n]] % mod
    else:
        for i in range(11, n+1):
            if i % 2: 
                for j in range(3, int(i ** .5) + 1, 2):
                    if i % j == 0: 
                        primecount.append(primecount[-1])
                        break
                else: 
                    primecount.append(primecount[-1] + 1)
            else: 
                primecount.append(primecount[-1])
        return factorial(n)[primecount[-1]] * factorial(n)[n - primecount[-1]] % mod