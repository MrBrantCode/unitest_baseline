"""
QUESTION:
Implement a function `find_sum` that calculates the sum of numbers in a list without using built-in sum functions or operators, using only a single loop, and with a time complexity of O(n), without utilizing any extra space or new variables. The input is a list of numbers and the output is the sum of these numbers.
"""

def find_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum