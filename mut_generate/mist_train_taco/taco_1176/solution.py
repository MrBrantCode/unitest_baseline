"""
QUESTION:
Your task is to calculate sum  of primes present as digits of given number N.
Example 1:
Input: 333
Output: 9
Explaination: 3 is a prime number. It 
is present 3 times. So 3+3+3 = 9.
Example 2:
Input: 686
Output: 0
Explaination: Neither 6 nor 8 is a 
prime number.
Your Task:
You do not need to read input or print anything. Your task is to complete the function primeSum() which takes N as input parameter and returns the sum of all the prime digits present in the number N.
Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 5*10^{4}
"""

import math

def prime_sum(N):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    sum_of_primes = 0
    while N > 0:
        digit = N % 10
        if is_prime(digit):
            sum_of_primes += digit
        N = N // 10
    
    return sum_of_primes