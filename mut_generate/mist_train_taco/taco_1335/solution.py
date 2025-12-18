"""
QUESTION:
Given two numbers n and x, find out the total number of ways n can be expressed as the sum of the Xth power of unique natural numbers. As the total number of ways can be very large, so return the number of ways modulo 10^{9 }+ 7. 
Example 1:
Input: 
n = 10, x = 2
Output: 
1 
Explanation: 
10 = 1^{2} + 3^{2}, Hence total 1 possibility. 
Example 2:
Input: 
n = 100, x = 2
Output: 
3
Explanation: 
100 = 10^{2} 
6^{2} + 8^{2} and 1^{2} + 3^{2} + 4^{2} + 5^{2} + 7^{2} 
Hence total 3 possibilities. 
Your Task:  
You don't need to read input or print anything. Complete the function numOfWays() which takes n and x as input parameters and returns the total number of ways n can be expressed as the sum of xth power of unique natural numbers.
Expected Time Complexity: O(n^{2}logn)
Expected Auxiliary Space: O(n)
Constraints:
1 <= n <= 10^{3}
1 <= x <= 5
"""

def count_ways_to_express_as_sum_of_powers(n: int, x: int) -> int:
    M = 1000000007
    powers = []
    i = 1
    while True:
        power = pow(i, x)
        if power <= n:
            powers.append(power)
            i += 1
        else:
            break
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for power in powers:
        for i in range(n, -1, -1):
            if i - power >= 0:
                dp[i] = (dp[i - power] + dp[i]) % M
    
    return dp[n]