"""
QUESTION:
Compute the sum of N(n) for all n in the range 1 to 10^8, where N(n) is the maximum length of an antichain of S(n), the set of factors of n. An antichain of S(n) is a subset A that comprises only a single element or none of the elements within A are divisible by any other elements of A.
"""

def antichain_sum(n):
    is_prime = [1]*(n+1)
    prime_factors = [0]*(n+1)

    for i in range(2, n+1):
        if is_prime[i] == 1:
            for j in range(i, n+1, i):
                is_prime[j] = 0
                prime_factors[j] += 1
    
    return sum(prime_factors)