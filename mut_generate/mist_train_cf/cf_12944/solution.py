"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of integers as input and returns a new list containing only the odd numbers from the original list, with no duplicates. The function should not use any built-in functions or libraries to remove duplicates.
"""

def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number % 2 != 0 and number not in new_list:
            new_list.append(number)
    return new_list