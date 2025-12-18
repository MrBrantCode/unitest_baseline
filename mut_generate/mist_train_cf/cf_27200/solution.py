"""
QUESTION:
Given an array of non-negative integers representing building heights, write a function `maxRectangleArea` that returns the maximum area of a rectangle that can be formed by selecting a contiguous sequence of buildings, where the width of the rectangle is the number of buildings selected and the height is the minimum height within the selected buildings. The input array will contain at least one building.
"""

from typing import List

def maxRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
    index = 0
    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = heights[top] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(max_area, area)
    while stack:
        top = stack.pop()
        area = heights[top] * ((index - stack[-1] - 1) if stack else index)
        max_area = max(max_area, area)
    return max_area