"""
QUESTION:
Write a function `filter_numbers` that takes a list of integers as input and returns a new list containing all the numbers from the input list that are not divisible by 3. The function should use a single loop and have a time complexity of O(n), where n is the length of the input list. Do not use any built-in functions or libraries.
"""

def filter_numbers(numbers):
    filtered_numbers = []
    
    for number in numbers:
        if number % 3 != 0:
            filtered_numbers.append(number)
    
    return filtered_numbers