"""
QUESTION:
Write a function `boxDelivering` that takes five parameters: `boxes`, `portsCount`, `maxBoxes`, `maxWeight`, and `maxFuel`, and returns the minimum number of trips a ship needs to make to deliver all boxes to their respective ports given the fuel constraints. The function should return -1 if it is not possible to deliver all boxes due to fuel constraints.

The `boxes` parameter is a list of lists where each sublist contains two integers: the port number and the weight of the box. The `portsCount`, `maxBoxes`, `maxWeight`, and `maxFuel` parameters are integers representing the number of ports, the maximum number of boxes the ship can carry, the maximum weight the ship can carry, and the maximum amount of fuel the ship can hold, respectively.
"""

def boxDelivering(boxes, portsCount, maxBoxes, maxWeight, maxFuel):
    n = len(boxes)
    boxes = [[0, 0]] + boxes + [[0, 0], [0, 0]]
    prefix = [0] *(n+4)
    dp, s = [0] * (n+4), [0] * (n+4)
    j = 0

    for i in range(1, n+1):
        while j < min(i, j + maxBoxes) and prefix[i] - prefix[j] <= maxWeight and i+2-j <= maxFuel:
            if boxes[j+1][0] != boxes[j][0]:
                maxFuel -= 1
            j += 1
        dp[i] = min(dp[j] + 2, dp[i-1] + 1) if j == i else min(dp[j] + 1, dp[i-1] + 1)
        s[i] = dp[i] if j == i else min(s[i-1], dp[i])
        dp[i] = min(dp[i], s[j] + 2)

    return dp[n]