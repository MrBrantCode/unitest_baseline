"""
QUESTION:
Given a list of integers representing the heights of consecutive buildings with a width of 1, find the area of the largest rectangle that can be formed, where the height of the rectangle is determined by the shortest building within it.

Write a function `largestRectangleArea` that takes in a list of integers `heights` and returns the area of the largest rectangle that can be formed.
"""

def largestRectangleArea(heights):
    stack = []
    heights.append(0)
    ans = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            ans = max(ans, h * w)
    return ans