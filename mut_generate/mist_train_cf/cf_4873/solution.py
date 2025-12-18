"""
QUESTION:
Implement a recursive function `reverse_list` to reverse a list of numbers and a separate function `print_reverse` to print the reversed list. The input list must contain at least 10 numbers. The program must handle the case when the input list is empty and print an appropriate message. It must also check for invalid input, such as non-numeric values in the list, and handle it gracefully. Do not use any built-in functions or methods to reverse the list.
"""

def reverse_list(numbers):
    if len(numbers) <= 1:
        return numbers

    return [numbers[-1]] + reverse_list(numbers[:-1])