"""
QUESTION:
Write a function named `find_three_elements` that takes an array `nums` of integers and an integer `target` as inputs. The function should return all possible combinations of three distinct elements from the array whose sum is equal to the given `target`. The array may contain duplicate numbers, but the three elements selected for the sum must be different. The time complexity requirement is O(n^2) and the space complexity requirement is O(n^2).
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