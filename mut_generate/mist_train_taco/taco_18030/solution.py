"""
QUESTION:
A Sphenic Number is a positive integer N which is product of exactly three distinct primes. The first few sphenic numbers are 30, 42, 66, 70, 78, 102, 105, 110, 114, …
Given a number N, your task is to find whether it is a Sphenic Number or not.
 
Example 1:
Input: N = 30
Output: 1
Explanation: 30 = 2 * 3 * 5 so N is 
product of 3 distinct prime numbers.
Example 2:
Input: N = 60
Output: 0
Explanation: 60 = 2 * 2 * 3 * 5 so N is
product of 4 prime numbers.
 
Your Task:
You don't need to read or print anyhting. Your task is to complete the function isSphenicNo() which takes N as input parameter and returns 1 if N is Sphenic Number otherwise returns 0.
 
Expected Time Complexity: O(N* log(N))
Expected Space Complexity: O(N)
 
Constraints:
1 <= N <= 1000
"""

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_sphenic_number(N):
    """Function to check if a number N is a Sphenic Number."""
    if N < 30:  # The smallest Sphenic Number is 30
        return 0
    
    prime_factors = []
    for i in range(2, N):
        if N % i == 0 and is_prime(i):
            prime_factors.append(i)
            if len(prime_factors) > 3:
                break
    
    if len(prime_factors) != 3:
        return 0
    
    if prime_factors[0] * prime_factors[1] * prime_factors[2] == N:
        return 1
    
    return 0