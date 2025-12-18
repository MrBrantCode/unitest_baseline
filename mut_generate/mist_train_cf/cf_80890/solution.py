"""
QUESTION:
Write a function named `second_highest` that takes a list of integers as input and returns the second-highest number in the list. The function should have a time complexity of O(n) and a space complexity of O(1). If there is no second-highest number (i.e., all numbers in the list are the same), the function should return the smallest possible integer value.
"""

def second_highest(numbers):
    max_num = second_max = float('-inf')
    
    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif second_max < num < max_num:
            second_max = num
    
    return second_max