"""
QUESTION:
Create a function named `sum_of_squares` that takes a list of numbers as input. The function should return the sum of squares of even integers in the list that are greater than or equal to 0 and less than or equal to 10. The function should ignore non-integer elements and return 0 if the list does not contain any even integers within the specified range.
"""

def sum_of_squares(numbers):
    even_numbers = [num for num in numbers if isinstance(num, int) and num % 2 == 0]
    filtered_numbers = [num for num in even_numbers if 0 <= num <= 10]
    squared_numbers = [num ** 2 for num in filtered_numbers]
    return sum(squared_numbers)