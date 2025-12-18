"""
QUESTION:
Define a function named `four_sum` that takes in a list of integers and a target sum as arguments. The function should return True if there exists a set of four unique numbers in the list that add up to the target sum, and False otherwise. The list may contain duplicate elements, and the function should have a time complexity of O(n^3), where n is the length of the list.
"""

def four_sum(nums, target):
    n = len(nums)
    nums = sorted(nums)

    for i in range(n-3):
        for j in range(i+1, n-2):
            left = j + 1
            right = n - 1
            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if curr_sum == target:
                    return True
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

    return False