"""
QUESTION:
Create a function `categorize_numbers` that takes a list of integers as input and returns two lists: one containing the odd numbers and the other containing the even numbers, both in ascending order. The function should use only a single loop to iterate through the input list.
"""

def categorize_numbers(numbers):
    odd_numbers = []
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

    odd_numbers.sort()
    even_numbers.sort()

    return odd_numbers, even_numbers