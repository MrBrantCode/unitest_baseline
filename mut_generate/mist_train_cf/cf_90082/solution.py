"""
QUESTION:
Create a function named `calculate_even_numbers` that takes a list of integers as input, classifies each integer as even or odd, calculates the sum of all the even integers in the list, and then finds the average of the even integers. The function should return the list of even numbers, the sum of even numbers, and the average of even numbers. If there are no even numbers in the list, the function should return an average of 0.
"""

def calculate_even_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    even_sum = sum(even_numbers)
    even_average = even_sum / len(even_numbers) if even_numbers else 0

    return even_numbers, even_sum, even_average