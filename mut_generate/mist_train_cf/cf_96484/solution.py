"""
QUESTION:
Implement a function `print_permutations(nums)` that prints all the permutations of the input list `nums` and returns the total number of permutations. You must implement the permutation algorithm from scratch without using any built-in functions or libraries that directly generate permutations. The input `nums` is a list of integers, and the function should print each permutation as a list and return the total count of permutations.
"""

def entrance(nums):
    count = 0

    def permute(nums, l, r):
        nonlocal count
        if l == r:
            print(nums)
            count += 1
        else:
            for i in range(l, r + 1):
                nums[l], nums[i] = nums[i], nums[l]
                permute(nums, l + 1, r)
                nums[l], nums[i] = nums[i], nums[l]  # backtrack

    permute(nums, 0, len(nums) - 1)
    return count