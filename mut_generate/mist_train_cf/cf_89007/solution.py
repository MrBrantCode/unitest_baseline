"""
QUESTION:
Write a function `sum_unique_numbers` that takes an array of integers as input and returns the sum of its unique elements. If the array has less than two elements, return `None`. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the number of elements in the array.
"""

def sum_unique_numbers(arr):
    if len(arr) < 2:
        return None

    unique_nums = []
    total = 0
    for num in arr:
        if num not in unique_nums:
            unique_nums.append(num)
            total += num
    
    return total