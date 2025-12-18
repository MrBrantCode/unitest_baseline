"""
QUESTION:
Given a number and its reverse. Find that number raised to the power of its own reverse.
Note: As answers can be very large, print the result modulo 10^{9} + 7.
Example 1:
Input:
N = 2
Output: 4
Explanation: The reverse of 2 is 2 and after raising power of 2 by 2 we get 4 which gives remainder as 4 when divided by 1000000007.
Example 2:
Input:
N = 12
Output: 864354781
Explanation: The reverse of 12 is 21and 12^{21} when divided by 1000000007 gives remainder as 864354781.
Your Task:
You don't need to read input or print anything. You just need to complete the function pow() that takes two parameters N and R denoting the input number and its reverse and returns power of (N to R)mod(10^{9} + 7).
Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(LogN).
Constraints:
1 <= N <= 10^{9}
"""

def calculate_power_modulo(N: int, R: int) -> int:
    MOD = 10**9 + 7
    
    def power(base: int, exponent: int) -> int:
        if exponent == 0:
            return 1
        half_power = power(base, exponent // 2)
        if exponent % 2 == 0:
            return (half_power * half_power) % MOD
        else:
            return (base * half_power * half_power) % MOD
    
    return power(N, R)