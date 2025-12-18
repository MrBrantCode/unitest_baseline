"""
QUESTION:
Write a function `trap` that calculates the total amount of water trapped between bars of given heights. The function should take a list of integers representing the heights of the bars and return an integer representing the total amount of water trapped. The width of each bar is 1. The function should have a time complexity of O(n) and a space complexity of O(n) where n is the number of bars.
"""

def trap(height):
    if not height:
        return 0
    
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = height[0]
    right_max[n - 1] = height[n - 1]
    
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    
    total = 0
    for i in range(n):
        total += max(0, min(left_max[i], right_max[i]) - height[i])
    
    return total