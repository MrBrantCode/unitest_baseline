"""
QUESTION:
Implement a function called `sum_of_even_numbers` that takes in a list of integers and returns the sum of all even numbers in the list using a for loop. The function should handle both positive and negative integers, ignore any non-integer elements in the list, and return 0 if there are no even numbers in the list. Additionally, you should not use any built-in functions or libraries to check if a number is even.
"""

def sum_of_even_numbers(numbers):
    sum = 0
    for num in numbers:
        if isinstance(num, int) and num % 2 == 0:
            sum += num
    return sum