"""
QUESTION:
Given an integer N, find the sum of GCD(i, N) where i = 1 to N. GCD denotes the greatest common divisor. Provide the answer modulus 10^{9} + 7.
Example 1:
Input: N = 2
Output: 3
Explanation:
GCD(1,2)+GCD(2,2) = 1 + 2 = 3
Ã¢â¬â¹Example 2:
Input: N = 10
Output: 27
Explanation:
GCD(1,10)+GCD(2,10)+...
+GCD(9, 10)+GCD(10, 10)=1+2+..+1+10=27
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sumOfGCDofPairs() which takes N as inputs and returns the answer.
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{6}
"""

def getCount(d, n):
    no = n // d
    result = no
    for p in range(2, int(pow(no, 1 / 2)) + 1):
        if no % p == 0:
            while no % p == 0:
                no //= p
            result -= result // p
    if no > 1:
        result -= result // no
    return result

def sum_of_gcd_of_pairs(N):
    MOD = 10**9 + 7
    res = 0
    n = N
    for i in range(1, int(pow(n, 1 / 2)) + 1):
        if n % i == 0:
            d1 = i
            d2 = n // i
            res += d1 * getCount(d1, n)
            if d1 != d2:
                res += d2 * getCount(d2, n)
    return res % MOD