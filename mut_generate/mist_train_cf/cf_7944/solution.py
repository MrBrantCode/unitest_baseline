"""
QUESTION:
Write a function named `check_occurrence` that takes two parameters: a list of integers and a target integer. The function should return `True` if the target integer occurs more than twice in the list and `False` otherwise. The time complexity of the function should be O(n), where n is the length of the input list.
"""

def check_occurrence(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
            if count > 2:
                return True
    return False