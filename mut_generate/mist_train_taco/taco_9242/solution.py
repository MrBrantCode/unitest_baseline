"""
QUESTION:
Mersenne Prime is a prime number that is one less than a power of two. In other words, any prime is Mersenne Prime if it is of the form 2^{k}-1 where k is an integer greater than or equal to 2. First few Mersenne Primes are 3, 7, 31 and 127.
The task is to find all Mersenne Primes smaller than equal to an input positive integer n.
 
Example 1:
Input: n = 10
Output: 3 7
Explanation:3 and 7 are only prime numbers
which are less than equal to 10 and in the
form of 2^{k} - 1. 
Example 2:
Input: n = 100
Output: 3 7 31
Explanation: 3, 7 and 31 are only prime
numbers which are less than equal to 100
and in the form of 2^{k} - 1.
Your Task:
You don't need to read or print anything. Your task is to complete the function AllMersennePrimeNo() which takes n as input parameter and returns a list of all Mersenne Primes less than or equal to n in sorted order.
Expected Time Complexity: O(n * log(log(n))
Expected Space Complexity: O(n)
Constraints: 
1 <= n <= 100000
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, max_div + 1):
        if n % i == 0:
            return False
    return True

def find_mersenne_primes(n):
    mersenne_primes = []
    k = 2
    while True:
        mersenne = (1 << k) - 1  # Equivalent to 2^k - 1
        if mersenne > n:
            break
        if is_prime(mersenne):
            mersenne_primes.append(mersenne)
        k += 1
    return mersenne_primes