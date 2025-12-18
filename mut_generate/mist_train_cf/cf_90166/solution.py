"""
QUESTION:
Write a function named `check_occurrence` that takes two parameters: a list of integers and a target integer. The function should return True if the target integer occurs in the list more than twice and False otherwise. The function should have a time complexity of O(n), where n is the length of the list, and should not use any built-in functions or libraries that provide direct solutions to the problem. The length of the input list is at most 10^6, the integers in the list are between -10^9 and 10^9, and the target integer is between -10^9 and 10^9.
"""

def check_occurrence(nums, target):
    count = 0
    for num in nums:
        if num == target:
            count += 1
            if count > 2:
                return True
    return False