"""
QUESTION:
Given two numbers L and R(L<R). Count all the prime numbers in the range [L, R].
Example 1:
Input:
L=1,R=10
Output:
4
Explanation:
There are 4 primes in this range, 
which are 2,3,5 and 7.
Example 2:
Input:
L=5,R=10
Output:
2
Explanation:
There are 2 primes in this range, 
which are 5 and 7.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countPrimes() which takes the two integers L and R as input parameters and returns the number of prime numbers in the range [L, R].
Expected Time Complexity:O(RLogLog(R))
Expected Auxillary Space:O(R)
Constraints:
1<=L<R<=2*10^{5}
"""

import math

def count_primes(L, R):
    primes = [True] * (R + 1)
    primes[0] = False
    primes[1] = False
    
    for i in range(2, int(math.sqrt(R)) + 1):
        if primes[i] == True:
            for j in range(i * i, R + 1, i):
                primes[j] = False
    
    cnt = 0
    for i in range(L, R + 1):
        if primes[i] == True:
            cnt += 1
    
    return cnt