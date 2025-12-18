"""
QUESTION:
Create a function called `filter_even_numbers` that takes a list of integers as input and returns a new list containing only the odd numbers from the original list. The input list contains integers ranging from -1000 to 1000. The function should not use any built-in functions or libraries.
"""

def filter_even_numbers(numbers):
    filtered_list = []
    for num in numbers:
        if num % 2 != 0:  # Check if number is odd
            filtered_list.append(num)
    return filtered_list