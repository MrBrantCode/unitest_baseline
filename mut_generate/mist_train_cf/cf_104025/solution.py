"""
QUESTION:
Write a function named `calculate_sums` that takes a list of integers as input. The function should return a tuple containing the sum of the squares of all the even numbers in the list and a list of the squares of all the odd numbers in the original list.
"""

def calculate_sums(numbers):
    even_sum = 0
    odd_squares = []
    
    for number in numbers:
        if number % 2 == 0:
            even_sum += number ** 2
        else:
            odd_squares.append(number ** 2)
            
    return even_sum, odd_squares