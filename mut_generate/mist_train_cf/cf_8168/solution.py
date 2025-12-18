"""
QUESTION:
Write a function called `split_list` that takes in a list of integers and returns two sublists with an equal sum and an equal number of elements. If it is not possible to split the list in such a way, the function should return `None`. The input list must have an even number of elements.
"""

def split_list(nums):
    def recursive_split(nums, index, sublist1, sublist2):
        if index == len(nums):
            if sum(sublist1) == sum(sublist2) and len(sublist1) == len(sublist2):
                return [sublist1, sublist2]
            else:
                return None

        sublist1.append(nums[index])
        result = recursive_split(nums, index + 1, sublist1, sublist2)
        if result:
            return result

        sublist1.pop()
        sublist2.append(nums[index])
        result = recursive_split(nums, index + 1, sublist1, sublist2)
        if result:
            return result

        sublist2.pop()
        return recursive_split(nums, index + 1, sublist1, sublist2)

    return recursive_split(nums, 0, [], [])