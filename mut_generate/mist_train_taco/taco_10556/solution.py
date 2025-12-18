"""
QUESTION:
People in Silverland use square coins. Not only they have square shapes but also their values are square numbers. Coins with values of all square numbers up to 289 (= 172), i.e., 1-credit coins, 4-credit coins, 9-credit coins, ..., and 289-credit coins, are available in Silverland.

There are four combinations of coins to pay ten credits:

* ten 1-credit coins,
* one 4-credit coin and six 1-credit coins,
* two 4-credit coins and two 1-credit coins, and
* one 9-credit coin and one 1-credit coin.



Your mission is to count the number of ways to pay a given amount using coins of Silverland.



Input

The input consists of lines each containing an integer meaning an amount to be paid, followed by a line containing a zero. You may assume that all the amounts are positive and less than 300.

Output

For each of the given amount, one line containing a single integer representing the number of combinations of coins should be output. No other characters should appear in the output.

Example

Input

2
10
30
0


Output

1
4
27
"""

def count_coin_combinations(amount: int) -> int:
    # Initialize the dp array with 1s, since there's always 1 way to make 0 (using no coins)
    dp = [1] * 300
    
    # Iterate over all square coins up to 17^2 (289)
    for i in range(2, 18):
        coin_value = i ** 2
        # Update the dp array for each coin value
        for j in range(coin_value, 300):
            dp[j] += dp[j - coin_value]
    
    # Return the number of combinations for the given amount
    return dp[amount]