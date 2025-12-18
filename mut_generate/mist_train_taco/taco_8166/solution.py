"""
QUESTION:
A magic number is defined as a number that can be expressed as a power of 5 or sum of unique powers of 5. First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
Given the value of n, find the n'th Magic number modulo 10^{9}+7.
Example 1:
Input: n = 1
Output: 5
Explanation: 1'st Magic number is 5.
Ã¢â¬â¹Example 2:
Input: n = 2
Output: 25
Explanation: 2'nd Magic number is 25. 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function nthMagicNo() which takes n input and returns the answer.
Expected Time Complexity: O(log n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n ≤ 10^{5}
"""

def nth_magic_number(n: int) -> int:
    MOD = 1000000007
    p = 5
    magic = 0
    while n:
        if n % 2 == 1:
            magic += p
        p *= 5
        n //= 2
    return magic % MOD