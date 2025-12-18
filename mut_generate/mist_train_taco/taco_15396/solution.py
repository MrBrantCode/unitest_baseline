"""
QUESTION:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:


Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

def calculate_trapped_water(height: list[int]) -> int:
    if not height:
        return 0
    
    result = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        if height[left] <= height[right]:
            tmp = height[left]
            left += 1
            while left < right and height[left] <= tmp:
                result += tmp - height[left]
                left += 1
        else:
            tmp = height[right]
            right -= 1
            while left < right and height[right] <= tmp:
                result += tmp - height[right]
                right -= 1
    
    return result