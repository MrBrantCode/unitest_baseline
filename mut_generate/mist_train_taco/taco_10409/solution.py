"""
QUESTION:
You are given a positive number N. Using the concept of Sieve, compute its prime factorisation.
Example:
Input: 
N = 12246
Output: 
2 3 13 157
Explanation: 
2*3*13*157 = 12246 = N.
Your Task:
Comple the function findPrimeFactors(), which takes a positive number N as input and returns a vector consisting of prime factors. You should implement Sieve algorithm to solve this problem.
 
Expected Time Complexity: O(Nlog(log(N)).
Expected Auxiliary Space: O(N).
Constraints:
1<=N<=2*10^{5}
"""

def prime_factorization(N):
    # Sieve of Eratosthenes to find all primes up to the square root of N
    max_limit = int(N**0.5) + 1
    is_prime = [True] * (max_limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(max_limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_limit + 1, i):
                is_prime[j] = False
    
    # Finding prime factors of N
    prime_factors = []
    for i in range(2, max_limit + 1):
        if is_prime[i]:
            while N % i == 0:
                prime_factors.append(i)
                N //= i
    
    # If N is still greater than 1, then it must be a prime number
    if N > 1:
        prime_factors.append(N)
    
    return prime_factors