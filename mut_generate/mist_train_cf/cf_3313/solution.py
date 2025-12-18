"""
QUESTION:
Implement a function called `sum_of_even_numbers` that takes in a list of elements as input and returns the sum of all even integers in the list. The function should ignore any non-integer elements and return 0 if there are no even numbers in the list. Note that the implementation should use a for loop, handle both positive and negative integers, and not use built-in functions or libraries to check if a number is even.
"""

def sum_of_even_numbers(lst):
    total = 0
    for num in lst:
        if isinstance(num, int) and num % 2 == 0:
            total += num
    return total