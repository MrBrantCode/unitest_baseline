"""
QUESTION:
Given two numbers n and k, find the k^{th} prime factor of n. 
Example 1:
Input: n = 225, k = 2
Output: 3
Explaination: The prime factors 3, 3, 5 
and 5. So 3 is the 2nd one.
Example 2:
Input: n = 81, k = 5
Output: -1
Explaination: The 4 prime factors are 
3, 3, 3, 3. So there is no 5th one.
Your Task:
You do not need to read input or print anything. Your task is to complete the function kthPrime() which takes the value n and k as input parameters and return the kth prime number. If k is greater than total number of primes then return -1.
Expected Time Complexity: O(n*log(log n))
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ n ≤ 10^{4}
1 ≤ k ≤ 50
"""

def kth_prime_factor(n: int, k: int) -> int:
    def is_prime(num: int) -> bool:
        """Helper function to check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_factors = []
    for i in range(2, n + 1):
        if is_prime(i):
            while n % i == 0:
                prime_factors.append(i)
                n //= i
    
    if len(prime_factors) >= k:
        return prime_factors[k - 1]
    else:
        return -1