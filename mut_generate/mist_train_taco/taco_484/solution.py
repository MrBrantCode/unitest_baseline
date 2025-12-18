"""
QUESTION:
Given two numbers L and R (inclusive) find the product of primes within this range. Print the product modulo 10^{9}+7. If there are no primes in that range you must print 1.
Example 1:
Input: L = 1, R = 10
Output: 210
Explaination: The prime numbers are 
2, 3, 5 and 7.
Example 2:
Input: L = 1, R = 20
Output: 9699690
Explaination: The primes are 2, 3, 
5, 7, 11, 13, 17 and 19.
Your Task:
You do not need to read input or print anything. Your task is to complete the function primeProduct() which takes L and R and returns the product of the primes within the range. If there are no primes in that range then return 1.
Expected Time Complexity: O((R-L)*(logR))
Expected Auxiliary Space: O(sqrt(R))
Constraints:
1 ≤ L ≤ R ≤ 10^{9}
0 ≤ L - R ≤ 10^{6}
"""

def prime_product(L, R):
    MOD = 10**9 + 7
    
    def sieve(n):
        """ Helper function to generate all primes up to n using the Sieve of Eratosthenes """
        primes = [1] * (n + 1)
        primes[0] = primes[1] = 0
        for i in range(2, n + 1):
            if primes[i] == 1:
                for j in range(i + i, n + 1, i):
                    primes[j] = 0
        return [i for i in range(2, n + 1) if primes[i] == 1]
    
    # Generate primes up to sqrt(R)
    sqrt_R = int(R ** 0.5)
    small_primes = sieve(sqrt_R)
    
    # Initialize a list to mark non-prime numbers in the range [L, R]
    is_prime = [1] * (R - L + 1)
    
    # Mark non-prime numbers in the range [L, R]
    for prime in small_primes:
        # Find the first multiple of prime >= L
        start = (L // prime) * prime
        if start < L:
            start += prime
        if start == prime:
            start += prime
        
        for multiple in range(start, R + 1, prime):
            is_prime[multiple - L] = 0
    
    # Calculate the product of primes in the range [L, R]
    product = 1
    for num in range(L, R + 1):
        if is_prime[num - L] == 1:
            product = (product * num) % MOD
    
    return product if product != 1 else 1