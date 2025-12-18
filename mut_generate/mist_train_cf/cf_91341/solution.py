"""
QUESTION:
Create a function called `sorted_odds` that takes a list of integers as input and returns a new list containing only the odd numbers from the input list, sorted in descending order with no duplicates. You are not allowed to use any built-in sorting or duplicate removal functions, such as `sorted()` or `set()`. The input list can contain up to 1 million elements.
"""

def sorted_odds(nums):
    """
    Returns a new list containing only the odd numbers from the input list, 
    sorted in descending order with no duplicates.

    :param nums: A list of integers
    :return: A list of unique odd integers in descending order
    """
    # Create a dictionary to store unique odd numbers
    odd_nums = {}
    for num in nums:
        if num % 2 != 0:
            odd_nums[num] = True

    # Implement a custom bubble sort to sort the odd numbers in descending order
    sorted_odds = list(odd_nums.keys())
    for i in range(len(sorted_odds)):
        for j in range(len(sorted_odds) - 1):
            if sorted_odds[j] < sorted_odds[j + 1]:
                sorted_odds[j], sorted_odds[j + 1] = sorted_odds[j + 1], sorted_odds[j]
    return sorted_odds