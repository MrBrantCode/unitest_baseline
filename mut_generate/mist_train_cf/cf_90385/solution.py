"""
QUESTION:
Create a function `num_ways_to_climb_stairs(n, k)` to calculate the number of different ways to climb `n` stairs when you can only climb `k` stairs at a time, where `k` is an arbitrary integer greater than or equal to 1. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def num_ways_to_climb_stairs(n, k):
    if n == 0:
        return 1
    
    dp = [0] * k
    dp[0] = 1
    
    for i in range(1, n+1):
        dp[i % k] = sum(dp)   # calculate the sum of all elements in dp
        
    return dp[n % k]