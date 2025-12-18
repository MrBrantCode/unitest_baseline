"""
QUESTION:
Ritika has a coin of  $N but she is the type of person who loves to have as much money as possible. A coin of $N can be exchanged in a bank into three coins of: $n/2, $n/3 and $n/4. But these numbers are all rounded down. Ritika decides to exchange her coin in the greed of money and makes profit. Your task is to find the maximum amout of money she can have at the end of exchange.
 
Example 1:
Input: N = 5
Output: 5
Explanation: 5 => 5/2 + 5/3 + 5/4 = 2 + 1 
+ 1 = 4 < 5 which means 5 can't be 
exchanged to earn profit so it itself is 
the maximum amount.
Example 2:
Input: N = 12
Output: 13
Explanation: 12 => 12/2 + 12/3 + 12/4 = 6 + 4
+ 3 = 13 (>12) after exchange.Now 6,4,3 can't 
be exchanged further to get profit.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function MaxExchangeMoney() which takes N as input parameter and returns maximum amount of money she can make by exchanging.
 
Expected Time Complexity:  O(log(N))
Expected Space Complexity: O(K) where K is constant.
 
Constraints:
1 <= N <= 10^{10}
"""

def max_exchange_money(N: int) -> int:
    dp = {}

    def maxm(n: int) -> int:
        if n == 0:
            return 0
        if n in dp:
            return dp[n]
        a = maxm(n // 3)
        b = maxm(n // 2)
        c = maxm(n // 4)
        dp[n] = max(n, a + b + c)
        return dp[n]
    
    return maxm(N)