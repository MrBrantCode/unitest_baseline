"""
QUESTION:
Given a list of integers and a target number, write a function named `fourSum` that finds all unique combinations of four numbers in the list that sum up to the target number. The function should take two parameters, `nums` (the list of integers) and `target` (the target number), and return a list of all unique combinations of four numbers that sum up to the target number. The function should handle duplicate numbers in the list by only returning unique combinations.
"""

def fourSum(nums, target):
    nums.sort()  # Sort the list to handle duplicates

    result = []
    n = len(nums)

    for i in range(n - 3):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            # Skip duplicates
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]

                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicates
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