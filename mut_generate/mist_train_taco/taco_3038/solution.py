"""
QUESTION:
Given a positive integer N, find the sum of all prime numbers between 1 and N(inclusive).
 
Example 1:
Input: N = 5
Output: 10
Explanation: 2, 3, and 5 are prime
numbers between 1 and 5(inclusive).
Example 2:
Input: N = 10
Output: 17
Explanation: 2, 3, 5 and 7 are prime
numbers between 1 and 10(inclusive).
 
Your Task:
You don't need to read or print anything. Your task is to complete the function prime_Sum() which takes N as input parameter and returns the sum of all primes between 1 and N(inclusive).
 
Expected Time Complexity: O(N*log(N))
Expected Space Complexity: O(N)
Constraints:
1 <= N <= 1000000
"""

import math

def sum_of_primes(N):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True
    
    sum_primes = 0
    for num in range(2, N + 1):
        if is_prime(num):
            sum_primes += num
    
    return sum_primes