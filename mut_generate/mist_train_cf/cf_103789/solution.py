"""
QUESTION:
Write a function named divide_even_odd that takes a list of positive integers as input and returns two lists: one containing the even numbers sorted in ascending order, and the other containing the odd numbers sorted in descending order.
"""

def divide_even_odd(lst):
    even = sorted([num for num in lst if num % 2 == 0])
    odd = sorted([num for num in lst if num % 2 != 0], reverse=True)
    return even, odd