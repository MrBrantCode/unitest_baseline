"""
QUESTION:
Implement a function `maxRectangleArea` that takes a list of integers representing building heights and returns the maximum area of a rectangle formed by a contiguous sequence of buildings. The width of each building is 1 unit, and the height of the rectangle is determined by the shortest building in the sequence. 

The function should be able to handle any list of building heights and return the maximum area of the rectangle that can be formed.
"""

def maxRectangleArea(heights):
    stack = []
    maxArea = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            maxArea = max(maxArea, heights[top] * width)
    while stack:
        top = stack.pop()
        width = i if not stack else len(heights) - stack[-1] - 1
        maxArea = max(maxArea, heights[top] * width)
    return maxArea