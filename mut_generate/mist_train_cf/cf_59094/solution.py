"""
QUESTION:
Write a function `findBags(nitrogenPerBag, target)` that takes an array `nitrogenPerBag` representing the amount of nitrogen per bag of each type and an integer `target` representing the target amount of nitrogen. The function should return the number of bags of each type needed to achieve the target amount of nitrogen. If the exact target amount cannot be achieved, return the combination that comes closest but does not exceed the target. The time complexity of the solution should be O(n*target).
"""

def findBags(nitrogenPerBag, target):
    n = len(nitrogenPerBag)

    # Initializing the dp array
    dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
    
    # Populate the dp array
    for i in range(1, n+1):
        for j in range(1, target+1):
            if nitrogenPerBag[i-1] <= j:
                dp[i][j] = max(nitrogenPerBag[i-1]+dp[i-1][j-nitrogenPerBag[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
            
    result = dp[n][target]

    # Get the nitrogen types used to achieve the result
    w = target
    bags = [0]*n
    for i in range(n, 0, -1):
        if result <= 0:
            break
        # either the result comes from the top (K[i-1][w]) 
        # or from (val[i-1] + K[i-1] [w-wt[i-1]]) as in Knapsack table. 
        # If it comes from the latter one/ it means the weight is included. 
        if result == dp[i - 1][w]:
            continue
        else:
            bags[i-1] += 1
            # Since this weight is included its 
            # value is deducted 
            result = result - nitrogenPerBag[i - 1]
            w = w - nitrogenPerBag[i - 1]
    return bags