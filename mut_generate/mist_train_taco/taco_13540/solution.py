"""
QUESTION:
Find ^{n}C_{r} for given n and r.
As answer can be very large, compute it modulo 10^{9} + 7.
Example 1:
Input: n = 3, r = 2
Output: 3
Explanation: ^{3}C_{2} = 3 
Ã¢â¬â¹Example 2:
Input: n = 4, r = 2
Output: 6
Explanation: ^{4}C_{2} = 6 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function ncr() which takes n and r as inputs and returns the answer modulo 10^{9} + 7.
Expected Time Complexity: O(n * log n)
Expected Auxiliary Space: O(n)
Constraints:
1 ≤ r, n ≤ 10^{5}
"""

def calculate_ncr(n: int, r: int) -> int:
    if r <= 0 or r > n:
        return 0
    
    mod = 1000000007
    num = 1
    den = 1
    
    for i in range(1, r + 1):
        num = num * n % mod
        den = den * i % mod
        n -= 1
    
    return num * pow(den, mod - 2, mod) % mod