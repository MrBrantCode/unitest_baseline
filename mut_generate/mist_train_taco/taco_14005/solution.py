"""
QUESTION:
Given a number N find the product of all unique prime factors of that number.
 
Example 1:
Input:
N = 5
Output:
5
Explanation:
5 has 1 prime factor 
i.e 5 only.
Example 2:
Input:
N = 24
Output:
6
Explanation:
24 has 2 prime factors 
3 and 2 where 3*2 = 6
Your Task:
You don't need to read input or print anything. Your task is to complete the function primeProduct() which takes an integer N as input parameters and returns an integer, product of all the prime factors of N.
 
Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(1)
 
Constraints:
1 <= N <= 10^{5}
"""

import math

def prime_product(N: int) -> int:
    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True
    
    product = 1
    for i in range(2, N + 1):
        if N % i == 0 and is_prime(i):
            product *= i
    return product