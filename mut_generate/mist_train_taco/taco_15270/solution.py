"""
QUESTION:
Given an integer array coins[ ] of size N representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ].  
Note: Assume that you have an infinite supply of each type of coin.  
Example 1:
Input:
sum = 4 , 
N = 3
coins[] = {1,2,3}
Output: 4
Explanation: Four Possible ways are:
{1,1,1,1},{1,1,2},{2,2},{1,3}.
Example 2:
Input:
Sum = 10 , 
N = 4
coins[] ={2,5,3,6}
Output: 5
Explanation: Five Possible ways are:
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} 
and {5,5}.
Your Task:
You don't need to read input or print anything. Your task is to complete the function count() which accepts an array coins[ ] its size N and sum as input parameters and returns the number of ways to make change for given sum of money. 
Expected Time Complexity: O(sum*N)
Expected Auxiliary Space: O(sum)
Constraints:
1 <= sum, N <= 10^{3}
"""

def count_ways_to_make_sum(coins: list[int], sum_value: int) -> int:
    # Initialize a table to store the number of ways to make each sum
    table = [0] * (sum_value + 1)
    table[0] = 1  # There's one way to make sum 0: use no coins
    
    # Iterate over each coin
    for coin in coins:
        # Update the table for all sums from coin to sum_value
        for j in range(coin, sum_value + 1):
            table[j] += table[j - coin]
    
    # The answer is the number of ways to make the given sum_value
    return table[sum_value]