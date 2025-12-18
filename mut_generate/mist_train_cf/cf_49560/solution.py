"""
QUESTION:
You are given an array of boxes with different colors represented by positive numbers, weights, and durability factors. You can choose continuous boxes with the same color, remove them, and get points calculated as k * k * w * d, where k is the number of boxes, w is the weight, and d is the durability factor. The task is to write a function `removeBoxes(boxes)` that returns the maximum points you can get, where boxes is a 2D array of integers, boxes[i] = [color, weight, durability].
"""

def removeBoxes(boxes):
    n = len(boxes)
    dp = [[[0]*100 for _ in range(100)] for _ in range(100)]
    
    def solve(l, r, k):       
        if l > r: 
            return 0
        if dp[l][r][k] != 0: 
            return dp[l][r][k]
            
        while (r > l) and (boxes[r][0] == boxes[r-1][0]):
            r -= 1
            k += 1
            
        res = solve(l, r-1, 0) + (k+1) * (k+1) * boxes[r][1] * boxes[r][2]       
        for i in range(l, r):
            if boxes[i][0] == boxes[r][0]:
                res = max(res, solve(l, i, k + 1) + solve(i+1, r-1, 0))
                
        dp[l][r][k] = res
        return res
 
    return solve(0, len(boxes) - 1, 0)