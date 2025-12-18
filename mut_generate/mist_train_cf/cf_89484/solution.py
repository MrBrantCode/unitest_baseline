"""
QUESTION:
Given a list of numbers and a target number, write a function `fourSum(nums, target)` that finds all unique combinations of four numbers in the list whose sum is equal to the target number. The function should return a list of lists, where each sublist contains four numbers that sum up to the target number. Assume that the input list may contain duplicate numbers, and the function should handle these duplicates to return unique combinations.
"""

def fourSum(nums, target):
    nums.sort()  

    result = []
    n = len(nums)

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return result