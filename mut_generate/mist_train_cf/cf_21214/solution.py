"""
QUESTION:
Design a function named `print_permutations` that takes a list of numbers as input and prints all possible permutations of the list. The function should return the total number of permutations. Implement the permutation algorithm from scratch without using any built-in functions or libraries that directly generate permutations.
"""

def print_permutations(nums):
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