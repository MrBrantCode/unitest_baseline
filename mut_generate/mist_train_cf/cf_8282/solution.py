"""
QUESTION:
Write a function `is_perfect_square(num)` that checks if a given number `num` is a perfect square and a function `determine_perfect_squares(numbers)` that takes a list of integers `numbers` and returns a new list with boolean values indicating whether each number in the input list is a perfect square or not. 

The input list can contain up to 10^6 integers, each between 1 and 10^12. The solution should not use built-in or external libraries for calculating square roots, powers, or arithmetic operations. It should have a time complexity of O(n) and a space complexity of O(n), where n is the number of integers in the input list.
"""

def is_perfect_square(num):
    guess = 1
    while guess * guess < num:
        guess += 1
    return guess * guess == num

def determine_perfect_squares(numbers):
    results = []
    for num in numbers:
        results.append(is_perfect_square(num))
    return results