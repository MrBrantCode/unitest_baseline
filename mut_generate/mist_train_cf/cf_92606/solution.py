"""
QUESTION:
Create a function `sort_numbers` that takes a list of numbers as input and returns a new list where all odd numbers are at the beginning (in their original order) followed by the even numbers in descending order. The function should not modify the original input list.
"""

def sort_numbers(numbers):
    odds = []
    evens = []

    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)

    evens.sort(reverse=True)

    return odds + evens