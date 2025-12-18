"""
QUESTION:
Write a function `sum_of_odd_numbers` that takes a list of integers as input and returns the sum of all the odd numbers in the list. The function must have a time complexity of O(n) and a space complexity of O(1).
"""

def sum_of_odd_numbers(numbers):
    sum_of_odds = 0
    for num in numbers:
        if num % 2 != 0:
            sum_of_odds += num
    return sum_of_odds