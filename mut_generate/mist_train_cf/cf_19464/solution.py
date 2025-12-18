"""
QUESTION:
Write a function `find_max_element` that takes an integer array as input, prints the number of times the maximum element occurs in the array, and returns a tuple containing the maximum element and its first occurrence index if the maximum element occurs more than once, or just the maximum element if it occurs only once.
"""

def find_max_element(nums):
    max_element = max(nums)
    max_count = nums.count(max_element)
    max_index = nums.index(max_element)
    
    if max_count > 1:
        print(f"The maximum element {max_element} occurs {max_count} times in the array.")
        return (max_element, max_index)
    else:
        print(f"The maximum element {max_element} occurs {max_count} time in the array.")
        return max_element