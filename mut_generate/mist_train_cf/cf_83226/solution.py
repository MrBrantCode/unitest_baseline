"""
QUESTION:
You are given several boxes with different colors represented by different positive numbers and weights associated with each box. Your goal is to remove boxes in rounds, choosing continuous boxes with the same color, and earn points calculated as `k * k * w`, where `k` is the number of boxes removed and `w` is the weight of the box. Implement the function `removeBoxes(boxes)` that returns the maximum points you can get, given the list of boxes as a list of tuples `(color, weight)`, with constraints `1 <= boxes.length <= 100` and `1 <= boxes[i][0], boxes[i][1] <= 100`.
"""

def removeBoxes(boxes):
    dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
    def get(i,j,k):
        if i>j: return 0
        if dp[i][j][k]==0:
            while (i+1<=j) and (boxes[i+1][0]==boxes[i][0]):
                i = i+1
                k = k+1
            dp[i][j][k] = get(i+1, j, 0) + (k+1)*(k+1)*boxes[i][1]
            for l in range(i+1,j+1):
                if boxes[l][0] == boxes[i][0]:
                    dp[i][j][k] = max(dp[i][j][k], get(i+1, l-1, 0) + get(l, j, k+1))
        return dp[i][j][k]
    
    return get(0, len(boxes)-1, 0)