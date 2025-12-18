"""
QUESTION:
Given a list of non-negative integers `height` representing the height of bars in a histogram, write a function `trap(height)` that calculates the amount of water that can be trapped between the bars. The function should return an integer representing the total amount of water that can be trapped. Note that the input list `height` may contain obstacles (negative numbers), which should be skipped when calculating the trapped water.
"""

def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    ans = 0

    while left < right:
        if height[left] < 0 or height[right] < 0:
            if height[left] < 0:
                left += 1
            if height[right] < 0:
                right -= 1
            continue

        if height[left] <= height[right]:
            if height[left] > max_left:
                max_left = height[left]
            else:
                ans += max_left - height[left]
            left += 1
        else:
            if height[right] > max_right:
                max_right = height[right]
            else:
                ans += max_right - height[right]
            right -= 1

    return ans