"""
QUESTION:
Create a function named `sort_numbers` that takes a list of integers as input and returns two separate lists: one containing all even numbers and the other containing all odd numbers. The function should return the two lists.
"""

def sort_numbers(numbers):
    even = []
    odd = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd