"""
QUESTION:
Write a function named `recursive_sum` that calculates the sum of the first `n` numbers in a given list using recursion. The main program should iterate over a list of numbers exactly 5 times using a `for` loop and track the sum of all the numbers encountered during each iteration. The list of numbers is `[1, 2, 3, 4, 5]`.
"""

def recursive_sum(numbers, n):
    if n == 0:
        return numbers[0]
    else:
        return numbers[n] + recursive_sum(numbers, n-1)