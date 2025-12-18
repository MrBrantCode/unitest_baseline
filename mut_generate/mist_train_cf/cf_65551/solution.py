"""
QUESTION:
Write a function `MoodyCoffeeShopOwner` that calculates the maximum satisfaction of a coffee shop owner given the number of customers, their corresponding moods (1 for moody, 0 for not moody), and two integers X and Y representing a time window and a delay, respectively. The function should return the maximum satisfaction, which is calculated based on the cumulative sum of customers and the number of moody customers within the time window. The function should handle cases where the time window or delay exceeds the number of customers.
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
            moody_customers[i+1] = moody_customers[i] + customers[i]
        else:
            moody_customers[i+1] = moody_customers[i]
        dp[i+1] = max(dp[i], cumulative[i+1])
        if i>=X-1:
            if i+Y+1<=n:
                dp[i+Y+1] = max(dp[i+Y+1], moody_customers[i+1]-(moody_customers[i-X+1] if i-X+1>=0 else 0)+cumulative[i-X+1])
            else:
                max_satisfaction = max(max_satisfaction, moody_customers[i+1]-((moody_customers[i-X+1]) if i-X+1>=0 else 0)+cumulative[i-X+1])
    return max_satisfaction