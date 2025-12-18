"""
QUESTION:
Ship all packages within D days while respecting package priority with the least weight capacity of the ship.

Create a function `shipWithinDays` that takes in three parameters: `weights` (a list of package weights), `priorities` (a list of package priorities), and `D` (the number of days to ship all packages). The function should return the least weight capacity of the ship that will result in all packages being shipped within D days while respecting the package priorities.

The ship's capacity should be at least the maximum weight of all packages and at most the total weight of all packages. Each day, packages can be loaded in the order given by `weights`, but packages with higher priority should be shipped earlier if possible. The length of `weights` and `priorities` is between 1 and 5 * 10^4, and each package's weight and priority are between 1 and 500.
"""

def shipWithinDays(weights, priorities, D):
    right, left = sum(weights), max(max(weights), sum(weights) // D)
    
    while left < right:
        mid, need, cur = (left + right) // 2, 1, 0
        weightPriority = list(zip(weights, priorities))
        weightPriority.sort(key = lambda x: -x[1])
        
        for weight, _ in weightPriority:
            if cur + weight > mid: 
                cur = 0
                need += 1
            cur += weight
        
        if need > D: 
            left = mid + 1
        else:            
            right = mid
            
    return left