"""
QUESTION:
Write a function `sum_unique_numbers(arr)` that takes an array of numbers as input, removes any duplicate numbers, and returns the sum of all unique numbers in the array. If the array has less than two elements, return `None`. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def entance(arr):
    if len(arr) < 2:
        return None

    unique_nums = set()
    total = 0
    for num in arr:
        if num not in unique_nums:
            unique_nums.add(num)
            total += num
    
    return total