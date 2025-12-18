"""
QUESTION:
Write a function named `separate_odd_even` that takes a list of integers as input and returns a list containing two sorted lists: one for even numbers and one for odd numbers, both in ascending order. The input list should have a length of at least 5 and at most 10^6, and each integer in the list should have a maximum value of 10^3.
"""

def separate_odd_even(arr):
    even_list = [num for num in arr if num % 2 == 0]
    odd_list = [num for num in arr if num % 2 != 0]
    even_list.sort()
    odd_list.sort()
    return [even_list, odd_list]