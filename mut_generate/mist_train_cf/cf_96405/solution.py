"""
QUESTION:
Implement a function find_three_sum(nums, target) that takes an array of positive integers and a target number as input, and returns all distinct sets of three numbers in the array that add up to the target number. The output should be in ascending order and contain no duplicates. The function should have a time complexity of O(n^2) or less.
"""

def find_three_sum(nums, target):
    nums.sort()  # Sort the array in ascending order
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:  # Skip duplicate elements
            continue
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicate elements
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result