"""
QUESTION:
You are given an array `customers` of length `n` representing the number of customers that enter the shop each minute, an array `moody` of the same length where `moody[i] = 1` if the shop owner is moody at minute `i` and `0` otherwise, and two integers `X` and `Y` representing the number of minutes the shop owner can remain not moody and then moody after using a secret technique, respectively. Your task is to return the maximum number of customers that can be satisfied throughout the day. Note that `1 <= X, Y < n <= 25000` and `0 <= customers[i], moody[i] <= 1500`. Write a function `MoodyCoffeeShopOwner(customers, moody, X, Y)` that solves this problem.
"""

def MoodyCoffeeShopOwner(customers, moody, X, Y):
    n = len(customers)
    cumulative = [0]*(n+1)
    for i in range(n):
        cumulative[i+1] = cumulative[i]+customers[i] if moody[i]==0 else cumulative[i]
    max_satisfaction = 0
    dp = [0]*(n+1)
    moody_customers = [0]*(n+1)
    for i in range(n):
        if moody[i]==1:
            moody_customers[i+1] = moody_customers[i]+customers[i]
        else:
            moody_customers[i+1] = moody_customers[i]  
        dp[i+1] = max(dp[i], cumulative[i+1])
        if i>=X-1:
            if i+Y+1<n:
                dp[i+Y+1] = max(dp[i+Y+1], moody_customers[i+1]-((moody_customers[i-X+1]) if i-X+1>=0 else 0)+cumulative[i-X+1])
            else:
                max_satisfaction = max(max_satisfaction, moody_customers[i+1]-((moody_customers[i-X+1]) if i-X+1>=0 else 0)+cumulative[i-X+1])
    return max_satisfaction