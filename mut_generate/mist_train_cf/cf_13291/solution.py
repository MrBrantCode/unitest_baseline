"""
QUESTION:
Implement a function called `add_numbers` that calculates the sum of all numbers in a given list. The function should have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(1). The function should not use any built-in functions or libraries to calculate the sum.
"""

def add_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total