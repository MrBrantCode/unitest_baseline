"""
QUESTION:
Create a function `get_max_triples(n, p)` that takes two positive integers `n` and `p` as input and returns the number of triples `(a[i], a[j], a[k])` where `i < j < k` from an array `a` of length `n` such that the modulus of the product of any two elements by the third `(a[i] * a[j]) % a[k]` is a multiple of either `n` or `p`. The array `a` is generated using the formula `a[i] = (i * i - i + p) + (i % p)` for each `i` from 1 to `n`.
"""

def get_max_triples(n, p):
    # calculate the array 'a' according to formula
    a = [(i * i - i + p) + (i % p) for i in range(1, n+1)]
    
    # initialize count of triples to 0
    counters = 0

    # consider all triples a[i], a[j], a[k] such that i < j < k
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # calculate modulus of product a[i]*a[j] by a[k]
                product_modulus = (a[i] * a[j]) % a[k]

                # check if the result is a multiple of n or p, increment the count
                if product_modulus % n == 0 or product_modulus % p == 0:
                    counters += 1

    return counters