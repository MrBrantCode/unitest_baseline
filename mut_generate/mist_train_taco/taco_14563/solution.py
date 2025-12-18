"""
QUESTION:
Given two numbers N and K. Find out if ‘N’ can be written as a sum of ‘K’ prime numbers.
Input:
N = 10 and K = 2
Output: 1
Explanation:
10 can be written as 5 + 5
 
Example 2:
Input:
N = 2 and K = 2
Output: 0
Your Task:  
You don't need to read input or print anything. Your task is to complete the function isSumOfKprimes() which takes the integer N and an integer K as input parameters and returns the true if N can be expressed as a sum of K primes else return false.
If function returns true, driver code will print 1 in output and 0 if the function returns false.
Expected Time Complexity: O(SQRT(N))
Expected Auxiliary Space: O(1)
 
 
Constraints:
1 <= N,K <= 10^{9}
"""

def is_sum_of_k_primes(N: int, K: int) -> bool:
    def is_prime(n: int) -> bool:
        if n == 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True
    
    if K == 1:
        return is_prime(N)
    
    if N % 2 == 0 and K == 2:
        return True
    
    if N % 2 == 1 and K == 2:
        return is_prime(N - 2)
    
    if K >= 3:
        return N >= 2 * K

    return False