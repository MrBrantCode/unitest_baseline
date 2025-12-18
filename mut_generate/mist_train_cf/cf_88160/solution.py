"""
QUESTION:
Write a function called `find_fourth_largest` that finds the fourth largest element in a list. The function should return the fourth largest element in the list. If the list has less than four distinct elements, the function should return None. The function should have a time complexity of O(n), where n is the number of elements in the list.
"""

def find_fourth_largest(nums):
    if len(nums) < 4:
        return None
    fourth_largest = float('-inf')
    for num in nums:
        if num > fourth_largest:
            fourth_largest = num
    for _ in range(3):
        max_value = float('-inf')
        for num in nums:
            if num > max_value and num < fourth_largest:
                max_value = num
        fourth_largest = max_value
    return fourth_largest