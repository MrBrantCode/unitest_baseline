"""
QUESTION:
Write a function named `sum_of_squares` that calculates the sum of squares of a given range of numbers. Using a while loop, print the first 20 positive integers in reverse order, excluding any numbers divisible by both 2 and 3. After printing the numbers, call the `sum_of_squares` function with a range of numbers from 1 to 20 and print the result.
"""

def sum_of_squares(n):
    return sum(i**2 for i in n)