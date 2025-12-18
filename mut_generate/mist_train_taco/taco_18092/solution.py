"""
QUESTION:
Given a number N, find the product of all the divisors of N (including N).
 
Example 1:
Input : 
N = 6
Output:
36
Explanation:
Divisors of 6 : 1, 2, 3, 6
Product = 1*2*3*6 = 36 
Example 2:
Input : 
N = 5
Output:
5
Explanation:
Divisors of 5 : 1, 5
Product = 1*5 = 5 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function divisorProduct() which takes integer N as input parameter and returns the product. Since the products may be very large, compute the answer modulo (10^{9}+ 7).
 
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{9}
"""

def divisor_product(N: int) -> int:
    mod = 10**9 + 7
    ans = 1
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            if N // i == i:
                ans = ans * i % mod
            else:
                ans = ans * i % mod
                ans = ans * (N // i) % mod
    return ans