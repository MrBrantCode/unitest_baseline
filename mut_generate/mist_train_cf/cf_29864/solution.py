"""
QUESTION:
Write a function `max_area` that takes a list of integers representing building heights and returns the maximum area that can be formed by selecting two buildings. The area is calculated by multiplying the minimum height of the two buildings by the distance between them. The function should return an integer representing the maximum area.
"""

def max_area(heights):
    max_area = 0
    left = 0
    right = len(heights) - 1
    
    while left < right:
        width = right - left
        h = min(heights[left], heights[right])
        area = width * h
        max_area = max(max_area, area)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_area