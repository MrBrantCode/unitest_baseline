"""
QUESTION:
Write a function called `split_list` that takes a list of integers as input and returns two lists. The first list should contain all odd numbers from the input list in their original order, and the second list should contain all even numbers from the input list in their original order. If the input list contains no odd or even numbers, the corresponding output list should be empty.
"""

def split_list(mylist):
    odd_numbers = [num for num in mylist if num % 2 != 0]
    even_numbers = [num for num in mylist if num % 2 == 0]
    return odd_numbers, even_numbers