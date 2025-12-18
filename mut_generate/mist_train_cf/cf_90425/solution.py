"""
QUESTION:
Implement a function `filter_numbers` that takes a list of integers between -1000 and 1000 as input and returns a new list with all numbers divisible by 3 removed. The function should only use a single loop and have a time complexity of O(n), where n is the length of the input list, and should not use any built-in functions or libraries.
"""

def filter_numbers(numbers):
    filtered_numbers = []
    
    for number in numbers:
        if number % 3 != 0:
            filtered_numbers.append(number)
    
    return filtered_numbers