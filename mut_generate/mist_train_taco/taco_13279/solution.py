"""
QUESTION:
Find the Euler Totient Function (ETF) Φ(N) for an input N. ETF is the count of numbers in {1, 2, 3, …, N} that are relatively prime to N, i.e., the numbers whose GCD (Greatest Common Divisor) with N is 1.
 
Example 1:
Input:
N = 11
Output:
10
Explanation:
From 1 to 11,
1,2,3,4,5,6,7,8,9,10
are relatively prime to 11.
Example 2:
Input:
N = 16
Output:
8
Explanation:
From 1 to 16
1,3,5,7,9,11,13,15 
are relatively prime
to 16.
Your Task:
You don't need to read input or print anything. Your task is to complete the function ETF() which takes one integer value N, as input parameter and return the value of Φ(N).
 
Expected Time Complexity: O(NLog N)
Expected Space Complexity: O(1)
 
Constraints:
1<=N<=10^{5}
"""

def euler_totient_function(N: int) -> int:
    x = N
    p = 2
    ans = N
    
    while p * p <= N:
        if x % p == 0:
            while x % p == 0:
                x = x // p
            ans = ans * (p - 1) // p
        p += 1
    
    if x > 1:
        ans = ans * (x - 1) // x
    
    return ans