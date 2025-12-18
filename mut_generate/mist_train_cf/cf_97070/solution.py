"""
QUESTION:
Given a list of 7 integers, implement a function `calculate_result` that performs the following operations in sequence: subtract the first number from the second, multiply the third by the fourth, add the result to the fifth, calculate the factorial of the sixth, and finally divide the factorial by the seventh number. Return the result of these operations.
"""

def calculate_result(numbers):
    result = numbers[1] - numbers[0]
    result *= numbers[2] * numbers[3]
    result += numbers[4]
    
    factorial = 1
    for i in range(1, numbers[5] + 1):
        factorial *= i
    
    result = factorial / numbers[6]
    return result