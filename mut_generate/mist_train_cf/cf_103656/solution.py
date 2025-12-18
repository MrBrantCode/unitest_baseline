"""
QUESTION:
Write a function called `count_even_numbers` that prints even numbers from 0 to a given upper limit (inclusive), excluding a specific number, and returns the sum of the printed numbers. The function should take two parameters: the upper limit and the number to exclude.
"""

def count_even_numbers(upper_limit, excluded_number):
    even_sum = 0
    for num in range(upper_limit + 1):
        if num % 2 == 0 and num != excluded_number:
            print(num)
            even_sum += num
    return even_sum