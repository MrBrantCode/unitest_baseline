"""
QUESTION:
Write a function named `split_list` that takes a list of numbers as input and returns two sets of numbers that have equal sums and an equal number of elements. The function should prioritize splitting the list into two sets with equal sum and an equal number of elements over splitting the list into two sets with just equal sum. If it is not possible to split the list into two sets with equal sum and an equal number of elements, the function should return an empty list. The input list can contain duplicate numbers and its sum is always even. The function should also consider that the number of elements in the list is always even.
"""

def split_list(nums):
    total_sum = sum(nums)
    target_sum = total_sum // 2
    
    nums.sort(reverse=True)  # sort the list in descending order
    
    set1 = []
    set2 = []
    
    for num in nums:
        if sum(set1) + num <= target_sum and len(set1) < len(nums) // 2:
            set1.append(num)
        else:
            set2.append(num)
    
    if sum(set1) == target_sum and len(set1) == len(nums) // 2:
        return [set1, set2]
    else:
        return []