"""
QUESTION:
Design a function called `permutations` that generates all unique permutations of a given list of numbers and returns them along with the total count of permutations. The function must implement a permutation algorithm from scratch without using any built-in permutation functions or libraries, handle duplicate numbers in the list, and have a time complexity of less than O(n!) where n is the length of the input list.
"""

def permutations(nums):
    result = []
    count = 0

    def backtrack(curr, nums, used):
        nonlocal count

        if len(curr) == len(nums):
            result.append(curr[:])
            count += 1
            return

        for i in range(len(nums)):
            if i in used:
                continue

            used.add(i)
            backtrack(curr + [nums[i]], nums, used)
            used.remove(i)

    backtrack([], nums, set())
    return result, count