"""
QUESTION:
Given an array of elements find all the prime factors of the LCM of the given numbers.
Example 1:
Input:
N = 8
Arr = {1 , 2, 3, 4, 5, 6, 7, 8}
Output: 2 3 5 7
Explaination: LCM of N elements is 840 
and 840 = 2*2*2*3*5*7.so prime factors 
would be 2, 3, 5, 7.
Example 2:
Input:
N = 4
Arr = {20, 10, 15, 60}
Output: 2 3 5
Explaination: LCM of N elements is 60
and 60 = 2*2*3*5.so prime factors
would be 2, 3, 5.
Your Task:
You don't need to read input or print anything. Your task is to complete the function primeFactorLcm() which takes the array Arr[] and its size N as input parameters and returns all the prime factors of the LCM of the given numbers.
Expected Time Complexity: O(Nsqrt(max(Arr_{i}))
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{4}
1 ≤ Arr_{i} ≤ 10^{4 }where 0≤i<N
"""

def prime_factors_of_lcm(Arr, N):
    from math import gcd
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    lc = Arr[0]
    for i in Arr:
        lc = lcm(lc, i)
    
    prime_factors = []
    d = 2
    while lc >= d:
        if lc % d == 0:
            while lc % d == 0:
                lc //= d
            prime_factors.append(d)
        d += 1
    
    return prime_factors