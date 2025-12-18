"""
QUESTION:
Write a program that includes two functions: sum_even_numbers(start, end) and average_odd_numbers(start, end). The sum_even_numbers function should calculate the sum of even numbers between start and end, while the average_odd_numbers function should calculate the average of odd numbers between start and end. The functions should be loosely coupled, have high cohesion, and promote separation of concerns. The program should also include a main part that uses these functions to calculate and print the sum of even numbers and the average of odd numbers between 1 and 100.
"""

def sum_even_numbers(start, end):
    """Calculate the sum of even numbers between start and end."""
    sum = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            sum += i
    return sum

def average_odd_numbers(start, end):
    """Calculate the average of odd numbers between start and end."""
    count = 0
    total = 0
    for i in range(start, end + 1):
        if i % 2 == 1:
            count += 1
            total += i
    if count > 0:
        return total / count
    else:
        return None