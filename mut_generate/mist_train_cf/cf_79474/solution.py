"""
QUESTION:
Write a function `find_triplet_sum(nums, target)` that takes a list of numbers `nums` and a target number `target` as input, and returns `True` if there exists a trio of elements in `nums` that sum up to `target`, and `False` otherwise. The function should have a time complexity of O(n^2) and should modify the input list if necessary.
"""

def find_triplet_sum(nums, target):
    nums.sort()

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return True
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return False