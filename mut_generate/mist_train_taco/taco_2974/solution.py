"""
QUESTION:
Given two integers n and r, find ^{n}C_{r. }Since the answer may be very large, calculate the answer modulo 10^{9}+7.
Example 1:
Input: n = 3, r = 2
Output: 3
Explaination: ^{3}C_{2} = 3. 
Example 2:
Input: n = 2, r = 4
Output: 0
Explaination: r is greater than n.
Your Task:
You do not need to take input or print anything. Your task is to complete the function nCr() which takes n and r as input parameters and returns ^{n}C_{r }modulo 10^{9}+7..
Expected Time Complexity: O(n*r)
Expected Auxiliary Space: O(r)
Constraints:
1 ≤ n ≤ 1000
1 ≤ r ≤ 800
"""

def calculate_nCr(n: int, r: int) -> int:
    MOD = 1000000007
    
    # Handle the case where r > n
    if r > n:
        return 0
    
    # Precompute factorials up to n
    factorials = [1] * (n + 1)
    for i in range(2, n + 1):
        factorials[i] = factorials[i - 1] * i % MOD
    
    # Calculate nCr using the precomputed factorials
    nCr = factorials[n] * pow(factorials[r], MOD - 2, MOD) % MOD
    nCr = nCr * pow(factorials[n - r], MOD - 2, MOD) % MOD
    
    return nCr