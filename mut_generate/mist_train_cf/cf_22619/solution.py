"""
QUESTION:
Write a function `split_list(nums)` that takes in a list of integers and splits it into two sublists with equal sum and an equal number of elements. If no such split is possible, return None. The input list is not guaranteed to have an even number of elements or elements that can be evenly divided into two sublists with equal sums.
"""

def split_list(nums):
    def helper(nums, index, sublist1, sublist2):
        if index == len(nums):
            if sum(sublist1) == sum(sublist2) and len(sublist1) == len(sublist2):
                return (sublist1, sublist2)
            else:
                return None

        sublist1.append(nums[index])
        result = helper(nums, index + 1, sublist1, sublist2)
        if result:
            return result

        sublist1.pop()
        sublist2.append(nums[index])
        result = helper(nums, index + 1, sublist1, sublist2)
        if result:
            return result

        return None

    return helper(nums, 0, [], [])