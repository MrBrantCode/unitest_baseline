"""
QUESTION:
Create a function named `group_numbers` that takes a list of integers as input. Group the numbers into two dictionaries - one for odd numbers and one for even numbers - where the keys are the numbers and the values are the frequencies of each number in the original list. Return or print these two dictionaries.
"""

def group_numbers(numbers):
    odd_numbers = {}
    even_numbers = {}
    for number in numbers:
        if number % 2 == 0:
            even_numbers[number] = even_numbers.get(number, 0) + 1
        else:
            odd_numbers[number] = odd_numbers.get(number, 0) + 1
    return odd_numbers, even_numbers