"""
QUESTION:
Write a function `find_combinations(nums, target)` that returns all distinct combinations of three elements from the given array `nums` where the sum of the elements in each combination is equal to the given target value. The array may contain duplicate elements, and there may be negative numbers.
"""

def find_combinations(nums, target):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if curr_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif curr_sum < target:
                left += 1
            else:
                right -= 1

    return result