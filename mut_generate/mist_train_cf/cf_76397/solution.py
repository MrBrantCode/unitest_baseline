"""
QUESTION:
Write a function called `findComplement(num)` that takes an integer `num` as input, where `1 <= num <= 2^31 - 1`, and returns its complement number. The complement strategy is to flip the bits of its binary representation at prime indices (1-indexed). The input integer is guaranteed to have no leading zero bits in its binary representation.
"""

def findComplement(num):
    def findPrimes(n):
        primes = []
        prime = [True for i in range(n+1)]
        p = 2
        while (p * p <= n):
            if (prime[p] == True):
                for i in range(p * p, n+1, p):
                    prime[i] = False
            p += 1
        for p in range(2, n):
            if prime[p]:
                primes.append(p)
        return primes

    bin_num = bin(num)[2:]   
    length = len(bin_num) 
    primes = findPrimes(length) 
    bits = list(bin_num) 
    for i in primes:
        if bits[length-i] == '1': 
            bits[length-i] = '0'
        else: 
            bits[length-i] = '1'
    return int(''.join(bits), 2)