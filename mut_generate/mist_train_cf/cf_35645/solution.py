"""
QUESTION:
Given an array of integers representing the heights of buildings, implement the `maxRectangleArea` function to find the maximum area of a rectangle that can be formed by a subset of these buildings, where the width of the rectangle is the number of buildings it covers and the height of the rectangle is the minimum height among the buildings it covers. The function should return the maximum area found. The input array will contain at least one element, and all elements are positive integers.
"""

def maxRectangleArea(heights):
    stack = []
    max_area = 0
    i = 0
    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)
    while stack:
        top = stack.pop()
        width = i if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, heights[top] * width)
    return max_area