"""
QUESTION:
Create a function `count_quadruples` that takes a list of unique positive and negative numbers as input and returns the number of quadruples in the list that sum up to zero, where a quadruple is defined as a set of four distinct numbers.
"""

def count_quadruples(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                for l in range(k+1, len(nums)):
                    if nums[i] != nums[j] != nums[k] != nums[l]:
                        if nums[i] + nums[j] + nums[k] + nums[l] == 0:
                            count += 1
    return count