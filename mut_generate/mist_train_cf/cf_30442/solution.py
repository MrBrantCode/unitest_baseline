"""
QUESTION:
Given an array of non-negative integers representing vertical line heights, write a function `maxArea` that calculates the maximum area formed between two vertical lines. The function takes a list of integers as input, where the length of the list is between 2 and 3 * 10^4, and returns the maximum area formed by using the shorter line as the height and the distance between the lines as the width. The distance between any two vertical lines is the difference in their indices.
"""

def maxArea(height):
    left = 0  
    right = len(height) - 1  
    max_area = 0  

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)  

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area