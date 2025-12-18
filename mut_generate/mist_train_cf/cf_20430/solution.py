"""
QUESTION:
Write a function `count_odd_numbers` that takes an array of integers as input and returns the count of odd numbers greater than 10 and less than 100, excluding negative numbers. The function should use a nested loop structure and store the qualifying odd numbers in a separate array before returning the count.
"""

def count_odd_numbers(array):
    odd_numbers = []
    for num in array:
        if num > 10 and num < 100 and num % 2 != 0:
            odd_numbers.append(num)
    return len(odd_numbers)