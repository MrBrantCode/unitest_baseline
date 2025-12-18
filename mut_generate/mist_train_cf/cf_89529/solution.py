"""
QUESTION:
Design a function `permutations(nums)` that prints all unique permutations of the given list of numbers and returns the total number of permutations. The function should handle duplicate numbers in the list and not use any built-in functions or libraries that directly generate permutations. The time complexity should be less than O(n!) where n is the length of the input list.
"""

def permutations(nums):
    result = []
    count = 0

    def backtrack(curr, nums, used):
        nonlocal count

        if len(curr) == len(nums):
            result.append(curr)
            count += 1
            return

        for i in range(len(nums)):
            if i in used or (i > 0 and nums[i] == nums[i-1] and i-1 not in used):
                continue

            used.add(i)
            backtrack(curr + [nums[i]], nums, used)
            used.remove(i)

    nums.sort()
    backtrack([], nums, set())
    return result, count