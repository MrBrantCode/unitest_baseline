"""
QUESTION:
Write a function `find_max_min` that takes a list of numbers as input and returns the maximum and minimum numbers in the list. Do not use any built-in functions or methods such as max(), min(), or sorting algorithms. The function should have a time complexity of O(n), where n is the length of the list, and handle edge cases such as an empty list, a list with a single element, negative numbers, large numbers, and duplicate numbers, without modifying the original list.
"""

def find_max_min(numbers):
    if len(numbers) == 0:
        return None, None
    
    max_num = numbers[0]
    min_num = numbers[0]
    
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    
    return max_num, min_num