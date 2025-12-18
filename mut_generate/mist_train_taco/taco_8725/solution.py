"""
QUESTION:
Find the nth Carol Number.
A Carol number is an integer of form 4^{n} – 2^{(n+1)} – 1. An equivalent formula is (2^{n}-1)^{2} – 2.
 
Example 1:
Input:
n = 2
Output:
7
Explanation:
After replacing the 
value of n in the 
formula we get 7.
 
Example 2:
Input:
n = 4
Output:
223
Explanation:
After replacing the 
value of n in the 
formula we get 223.
 
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function nthCarolNumber() which takes an integer n and returns the value mod 10^{9}+7.
 
Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= n <= 10^{9}
"""

def nth_carol_number(n: int) -> int:
    m = 10**9 + 7
    b = 1
    a = 2
    
    while n != 1:
        if n % 2:
            b = b * a % m
            n = (n - 1) // 2
        else:
            n = n // 2
        a = a ** 2 % m
    
    return ((a * b - 1) ** 2 - 2) % m