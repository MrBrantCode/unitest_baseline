"""
QUESTION:
Implement a function named `count_numbers` that takes a list of numbers as input and returns the count of odd numbers and even numbers in the list using recursion. The list can be of any length. The function should not take any other parameters besides the list of numbers.
"""

def count_numbers(numbers):
    if len(numbers) == 0:  # base case: no more numbers to count
        return (0, 0)  # return count of odd and even numbers as (0, 0)
    else:
        num = numbers[0]  # get the first number in the list
        (odd_count, even_count) = count_numbers(numbers[1:])  # recursively count numbers in the rest of the list
        if num % 2 == 0:  # if the number is even
            return (odd_count, even_count + 1)  # return updated count of odd and even numbers
        else:  # if the number is odd
            return (odd_count + 1, even_count)  # return updated count of odd and even numbers