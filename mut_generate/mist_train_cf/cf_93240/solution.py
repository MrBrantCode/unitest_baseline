"""
QUESTION:
Write a function `multiply_odd_and_square_even` that takes a list of integers as input. For each number in the list, multiply it by 5 if it's odd and replace it with its square if it's even. Return the resulting list, maintaining the original order.
"""

def multiply_odd_and_square_even(lst):
    result = []
    for num in lst:
        if num % 2 == 1:
            result.append(num * 5)
        else:
            result.append(num ** 2)
    return result