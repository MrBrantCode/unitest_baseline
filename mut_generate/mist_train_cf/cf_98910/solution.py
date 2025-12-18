"""
QUESTION:
Create a function `sum_of_even_numbers` that takes a list of integers as input and returns the sum of all even numbers in the list. The function should handle edge cases such as empty lists, non-integer values, and negative numbers, and should have a linear time complexity of O(n) and a space complexity of O(1).
"""

def sum_of_even_numbers(numbers):
    total = 0
    for number in numbers:
        if isinstance(number, int) and number % 2 == 0:
            total += number
    return total