"""
QUESTION:
Write a function `multiply_odd_and_square_even(lst)` that takes a list of integers as input. For each number in the list, if the number is odd, multiply it by 5; if the number is even, replace it with its square. The function should return a new list containing the modified numbers in the original order.
"""

def multiply_odd_and_square_even(lst):
    result = []
    for num in lst:
        if num % 2 == 1:
            result.append(num * 5)
        else:
            result.append(num ** 2)
    return result