"""
QUESTION:
Write a function `numTrees(n)` to calculate the total number of possible binary trees with `n` nodes. The function should return an integer representing the total number of possible binary trees. Assume that the input `n` is a non-negative integer.
"""

def numTrees(n): 
    if n == 0: 
        return 1
    else: 
        num = 0
        for roots in range(1, n+1): 
            leftNum = numTrees(roots - 1) 
            rightNum = numTrees(n - roots) 
            num += leftNum * rightNum 
    return num