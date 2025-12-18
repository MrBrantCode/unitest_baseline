"""
QUESTION:
Write a function `find_three_elements` that takes an array `nums` and a target sum `target` as inputs, and returns all possible combinations of three distinct elements from `nums` whose sum is equal to `target`. The function should have a time complexity of O(n^2) and a space complexity of O(n^2). The input array may contain duplicate numbers, but the three elements selected for the sum must be different.
"""

def find_three_elements(nums, target):
    nums.sort()  
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1  

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1  

            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result