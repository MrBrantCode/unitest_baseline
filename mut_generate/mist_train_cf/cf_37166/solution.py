"""
QUESTION:
Write a function `threeSumClosest(nums, target)` that takes in a sorted or unsorted array of integers `nums` and an integer `target` as input and returns the sum of three integers in the array that is closest to the target. The function should consider all possible combinations of three integers in the array and return the sum that has the smallest absolute difference with the target.
"""

def threeSumClosest(nums, target):
    nums.sort()  # Sort the array
    closest_sum = float('inf')  # Initialize closest sum to positive infinity
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1  # Two pointers approach
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum  # Update closest sum if current sum is closer to target
            if current_sum < target:
                left += 1  # Move left pointer to the right
            elif current_sum > target:
                right -= 1  # Move right pointer to the left
            else:
                return current_sum  # Return early if the sum equals the target
    return closest_sum  # Return the closest sum found