"""
QUESTION:
Implement a function called `power_set` that takes a list of integers as input and returns a list of lists representing the power set of the input list, including the empty set and the set itself, without using any built-in functions or libraries to directly compute the power set. The function should handle the case where the input list is empty.
"""

def power_set(nums):
    if not nums:
        return [[]]  

    element = nums[0]  
    remaining_set = nums[1:]  

    subsets = power_set(remaining_set)

    power_set_with_element = subsets + [subset + [element] for subset in subsets]

    return power_set_with_element