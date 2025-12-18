"""
QUESTION:
Find all pairs (sets) of prime numbers (p,q) such that p*q <= n, where n is given number. 
 
Example 1:
Input: n = 4
Output: 2 2
Explanation: Pair (2, 2) which has both prime 
numbers as well as satisfying the condition 
2*2 <= 4.
Example 2:
Input: n = 8
Output: 2 2 2 3 3 2
Explanation: Pairs(2, 2), (2, 3) and (3, 2)
which has both prime numbers and satisfying
the given condition.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function prime_pairs() which takes n as input parameter and returns a list of pairs in ascending order.
 
Expected Time Complexity: O(n^{2}* sqrt(n))
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 400
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_pairs(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    pairs = []
    for i in range(len(primes)):
        for j in range(len(primes)):
            if primes[i] * primes[j] <= n:
                pairs.append(primes[i])
                pairs.append(primes[j])
    return pairs