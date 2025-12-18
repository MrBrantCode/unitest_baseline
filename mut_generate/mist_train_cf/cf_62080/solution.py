"""
QUESTION:
Compute the amount of rainwater that can be trapped in an elevation map with obstacles. The elevation map is represented by an array of integers, where the width of each bar is 1. Obstacles are represented by negative integers and water cannot be trapped on them. 

Create a function `trap(height)` that takes an array of integers as input and returns the total amount of rainwater that can be trapped. The length of the input array `n` is between 0 and 3 * 10^4 (inclusive), and each element in the array is between -10^5 and 10^5 (inclusive).
"""

def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    max_left, max_right = 0, 0
    ans = 0

    while left < right:
        # If there is an obstacle, it moves the pointers inward.
        if height[left] < 0 or height[right] < 0:
            if height[left] < 0:
                left += 1
            if height[right] < 0:
                right -= 1
            continue

        # If the left bar is shorter than the right, process the left bar first.
        if height[left] <= height[right]:
            # If the current left bar is higher than max_left, it cannot trap any water.
            # Thus, update max_left.
            if height[left] > max_left:
                max_left = height[left]
            # Otherwise, the current left bar can trap water with the height `max_left - height[left]`.
            else:
                ans += max_left - height[left]
            left += 1

        # If the right bar is shorter than the left, process the right bar first.
        else:
            # If the current right bar is higher than max_right, it cannot trap any water.
            # Thus, update max_right.
            if height[right] > max_right:
                max_right = height[right]
            # Otherwise, the current right bar can trap water with the height `max_right - height[right]`.
            else:
                ans += max_right - height[right]
            right -= 1

    return ans