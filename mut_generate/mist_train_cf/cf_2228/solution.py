"""
QUESTION:
Implement the quick_sort function to sort a list of integers from least to greatest. The function should have a time complexity of O(n log n) in the average case and be able to handle lists with duplicate elements.
"""

def entrance(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    lesser_nums = [x for x in numbers[1:] if x < pivot]
    greater_nums = [x for x in numbers[1:] if x >= pivot]
    return entrance(lesser_nums) + [pivot] + entrance(greater_nums)