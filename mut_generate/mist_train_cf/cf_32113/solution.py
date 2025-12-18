"""
QUESTION:
Create a function `process_numbers` that takes a list of integers as input. The function should calculate the square of each number in the list, sum all the squared numbers, and check if the sum is even or odd. If the sum is even, raise a custom exception `EvenSumException` with the message "Even sum found". If the sum is odd, return the sum. Handle the `EvenSumException` by catching it and printing the exception message.
"""

class EvenSumException(Exception):
    pass

def entrance(numbers):
    try:
        squared_numbers = [num ** 2 for num in numbers]
        sum_of_squares = sum(squared_numbers)
        if sum_of_squares % 2 == 0:
            raise EvenSumException("Even sum found")
        else:
            return sum_of_squares
    except EvenSumException as e:
        print(e)