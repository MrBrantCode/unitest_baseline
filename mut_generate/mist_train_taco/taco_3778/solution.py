"""
QUESTION:
People in Cubeland use cubic coins. Not only the unit of currency is called a cube but also the coins are shaped like cubes and their values are cubes. Coins with values of all cubic numbers up to 9261 (= 213), i.e., coins with the denominations of 1, 8, 27, ..., up to 9261 cubes, are available in Cubeland.
Your task is to count the number of ways to pay a given amount using cubic coins of Cubeland. For example, there are 3 ways to pay 21 cubes: twenty one 1 cube coins, or one 8 cube coin and thirteen 1 cube coins, or two 8 cube coin and five 1 cube coins.

Input

First line of input contains the total number of test cases T.
Next T lines contains amount to be paid. You may assume that all the amounts are positive and less than 10000.

Output

For each of the given amounts to be paid output one line containing a single integer representing the number of ways to pay the given amount using the coins available in Cubeland.

SAMPLE INPUT
2
2
10

SAMPLE OUTPUT
1
2
"""

def count_ways_to_pay(amount: int) -> int:
    # Precompute the cubic coins up to 21^3
    cubic_coins = [i**3 for i in range(1, 22)]
    
    # Initialize the array to store the number of ways to pay each amount
    ways = [0] * 10001
    ways[0] = 1  # There's one way to pay 0 amount: use no coins
    
    # Fill the ways array using dynamic programming
    for coin in cubic_coins:
        for i in range(coin, 10001):
            ways[i] += ways[i - coin]
    
    # Return the number of ways to pay the given amount
    return ways[amount]