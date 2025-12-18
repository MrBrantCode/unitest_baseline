"""
QUESTION:
Given a number N find the sum of the Euler Totient values of all the divisors of N.
 
Example 1:
Input:
N = 5
Output:
5
Explanation:
1 and 5 are the factor 
of 5 and Φ(1) = 1 and
Φ(5) = 4 and their sum
is 4 + 1 = 5
Example 2:
Input:
N = 1
Output:
1
Explanation:
1 is the only factor of
1 and Φ(1) = 1
Your Task:
You don't need to read input or print anything. Your task is to complete the function phiSum() which takes an integer N as input parameter and returns an integer, sum of the Euler Totient values of all the divisors of N.
 
Expected Time Complexity: O(1)
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{6}
"""

def phiSum(N):
    def euler_totient(n):
        result = n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n //= p
                result -= result // p
            p += 1
        if n > 1:
            result -= result // n
        return result
    
    total_sum = 0
    for i in range(1, N + 1):
        if N % i == 0:
            total_sum += euler_totient(i)
    
    return total_sum