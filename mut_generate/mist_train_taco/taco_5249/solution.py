"""
QUESTION:
Given a number N. Calculate the product of all factors of N. Since Answer can be very large,compute the answer modulo 10^{9}+7.
Example 1:
Input:
N=6
Output:
36
Explanation:
Factors of 6 are 1,2,3,6.Their product is
(1*2*3*6)%(10^{9}+7)=36.
Example 2:
Input:
N=25
Output:
125
Explanation:
The factors of 25 are 1,5 and 25.
So, Their product is (1*5*25)%(10^{9}+7)
=125.
Your Task:
You don't need to read input or print anything.Your task is to complete the function factorProduct() which takes a number N as input parameter and returns the product of all factors of N.
Expected Time Complexity:O(Sqrt(N))
Expected Auxillary Space:O(1)
Constraints:
1<=N<=10^{9}
"""

import math

def calculate_factor_product(N: int) -> int:
    MOD = 1000000007
    product = 1
    
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if i == N // i:
                product = product * i % MOD
                break
            product = product * i % MOD
            product = product * (N // i) % MOD
    
    return product