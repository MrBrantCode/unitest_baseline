"""
QUESTION:
Create a function called "reverse_print_sum" that takes a list of integers as input. The function should iterate over the list in reverse order, printing each element's value. It should also calculate and return the sum of all the values in the reversed order. The function should not take any additional parameters and should not use any global variables.
"""

def reverse_print_sum(arr):
    total_sum = 0
    for num in reversed(arr):
        print(num)
        total_sum += num
    return total_sum