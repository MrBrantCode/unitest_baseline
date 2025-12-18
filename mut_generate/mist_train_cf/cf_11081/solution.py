"""
QUESTION:
Write a function `filter_numbers` that takes a list of numbers and a target number as input, and returns a new list containing only the numbers greater than the target, without any duplicates. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

def filter_numbers(numbers, target):
    filtered_list = []
    seen = set()
    
    for num in numbers:
        if num > target and num not in seen:
            filtered_list.append(num)
            seen.add(num)
    
    return filtered_list